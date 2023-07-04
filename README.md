# Google Drive Shared Files Scanner and Remover

This script lists all the files in your Google Drive account that are shared with others. Additionally, it can remove shared access when run with the `--delete` argument.

## ⚠️ Warning
This script can remove permissions from all shared files, including those shared with third-party apps that rely on these permissions for their functionality. This could lead to unintended consequences, such as breaking connections with apps that rely on these permissions, including but not limited to backup and recovery services like WhatsApp.

It is strongly recommended that users first manually review the shared files identified by the script.

Only after carefully reviewing the list should you consider running the script in delete mode. And even then, proceed with caution. Always be aware of the potential consequences and make sure you're making an informed decision.

Remember: once permissions are removed, the process cannot be easily reversed. Always double-check before you remove sharing permissions.
**You can remove the permissions manually one-by-one**.

Please use this script responsibly and double-check the files whose permissions you are removing.

Here's a list of some well-known third-party apps that commonly use Google Drive for various functionalities such as backup, syncing, and data storage:

1. **WhatsApp**: This popular messaging app offers a backup feature that uses Google Drive to store chat histories, images, and videos.
2. **Slack**: Slack can integrate with Google Drive, allowing users to share files directly from their Drive.
3. **Asana**: This project management tool can attach Google Drive files directly to tasks.
4. **Trello**: Trello cards can link directly to files in Google Drive.
5. **Zapier**: This online automation tool connects Google Drive with hundreds of other apps and services for automated workflows.
6. **DocuSign**: This electronic signature technology allows users to sign documents directly from Google Drive.
7. **Evernote**: This app can backup and sync notes with Google Drive.
8. **IFTTT**: This web-based service creates applets that can automate saving certain types of files (like photos, documents, etc.) to Google Drive.
9. **Autodesk AutoCAD**: This app allows you to open DWG files from Google Drive directly in the AutoCAD web app.
10. **Adobe Creative Cloud**: Adobe's suite of tools can integrate with Google Drive for storing and sharing creative files.
11. **Smartsheet**: This work execution platform enables users to attach files from Google Drive directly to individual task rows.
12. **Airtable**: Users can attach files directly from Google Drive to any record in their Airtable bases.
13. **Lucidchart and Lucidpress**: These tools integrate with Google Drive, allowing users to collaborate on diagrams and digital publishing directly from Drive.
14. **Zoom**: Zoom can record video meetings and save them directly to Google Drive.
15. **Backup and Sync from Google**: This is Google's official client for syncing files from your Google Drive to your local computer and vice versa.
16. **Google Workspace (formerly G Suite)**: This suite of productivity apps from Google (including Gmail, Docs, Sheets, Slides, and more) integrates closely with Google Drive for storage and collaboration.
17. **Pixlr**: Pixlr, an online photo editor, can store and open images directly from Google Drive.
18. **HelloFax**: This tool allows you to send faxes directly from Google Drive.
19. **ManyChat**: In ManyChat, a chatbot platform, you can use Google Drive to store user data and files gathered from the bot.
20. **XMind**: This mind mapping tool can save and load mind maps directly from Google Drive.
21. **PandaDoc**: This document automation software allows you to import, export, and store documents in Google Drive.
22. **Coggle**: This collaborative mind-mapping tool can save mind maps to Google Drive.
23. **draw.io (also known as diagrams.net)**: This diagramming application can save your diagrams directly to Google Drive.
24. **UpdraftPlus**: A popular WordPress plugin that can back up your website directly to Google Drive.
25. **Keeper**: This password manager can export backups of your vault to Google Drive.

Remember, this script could potentially disrupt services from these apps that rely on file sharing permissions, so be cautious when using it. Always double-check the files and permissions you're altering to avoid unwanted results.


## Getting Started

Follow these instructions to get the project running on your machine:

### Prerequisites

- Python 3.6 or above
- `google-auth`, `google-auth-httplib2`, `google-auth-oauthlib`, `google-api-python-client`, `httplib2`

Install the prerequisites by running:

```bash
pip install --upgrade google-auth google-auth-httplib2 google-auth-oauthlib google-api-python-client httplib2
```


### Google API setup

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. From the projects list, select a project or create a new one.
3. If the APIs & services page isn't already open, open the console left side menu and select **APIs & services**.
4. On the left, click **Library**.
5. In the search box, enter "Drive" and select "Google Drive API".
6. Click **ENABLE** to enable the Drive API for your project.
7. On the left, click **Credentials**.
8. Click **+ Create Credentials**, then select **OAuth client ID**.
9. If you're creating credentials for the first time, you need to configure the consent screen. Click **Configure consent screen** and fill out the form.
10. After you've configured the consent screen, you will be redirected back to the credentials screen. If not, click **Create Credentials** again and select **OAuth client ID**.
11. For **Application type**, choose **Desktop app** and create.
12. You will now see your **Client ID** and **Client Secret**. Click **OK**.
13. Next to the newly created OAuth 2.0 client, click the download button to download your `credentials.json` file.
14. Save the `credentials.json` file to the directory where the Python script is located.

## Usage

There are two modes of operation: scan-only and delete mode.

### Scan-Only Mode

This mode will only list the files and folders in your Google Drive that are shared with others.

To run the script in scan-only mode, use:

```bash
python drive_scanner.py
```


### Delete Mode

This mode will list the shared files and folders, and also remove all shared access.

**Warning**: Use this mode with caution. It will unshare all files and folders shared with others.

To run the script in delete mode, use:

```bash
python drive_scanner.py --delete
```


## Notes

When you run the script for the first time, it will open a new browser window for you to log in with your Google account. Log in and allow the requested permissions. This will create a new `token.json` file with the necessary OAuth 2.0 credentials for the script to use.

If the script is not working as expected, delete the `token.json` file and run the script again to generate new credentials.

