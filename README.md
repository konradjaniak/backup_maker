# backup_maker
Takes source path to the folder and creates a ZIP backup of it in given interval to the destination folder

## How it works
Get into folder you want to create backup of. Copy the path. Paste the path into the source input. Put anything in destination input (it doesn't do anything but it cannot be empty). There is no validation of the input, so make sure that the path provided is valid. The app will create a folder one level above and it will be called SOURCEFOLDER_BACKUP (ex. MyProject_BACKUP). Inside that folder there will be copy folders with date and time added to the folder name (ex. MyProject_2020_07_15_21_33_15). Backup is made every 30 minutes.

Example files tree:

-> ProjectFolder
-> ProjectFolder_BACKUP
	-> ProjectFolder_2020_07_15_20_15_23
	-> ProjectFolder_2020_07_15_20_45_23