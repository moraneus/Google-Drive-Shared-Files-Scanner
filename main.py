import argparse
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# Define the scopes (permissions) you need
SCOPES = ['https://www.googleapis.com/auth/drive']


def main(delete):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json') and os.path.getsize('token.json') > 0:
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)

    # Call the Drive v3 API
    service = build('drive', 'v3', credentials=creds)

    # Start the list request
    request = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name, owners)")

    while request is not None:
        results = request.execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            for item in items:
                if item['owners'][0]['me']:
                    # Check the permissions of the file
                    permissions = service.permissions().list(fileId=item['id']).execute().get('permissions', [])
                    for permission in permissions:
                        # If there are more permissions than just the owner
                        if permission['role'] != 'owner':
                            print(f"Shared file: {item['name']} ({item['id']})")
                            if delete:
                                print(f"Removing permission from file: {item['name']} ({item['id']})")
                                service.permissions().delete(fileId=item['id'], permissionId=permission['id']).execute()
        # Go to the next page
        request = service.files().list_next(request, results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan and/or remove shared permissions on Google Drive.')
    parser.add_argument('--delete', action='store_true', help='Delete shared permissions')
    args = parser.parse_args()

    main(args.delete)
