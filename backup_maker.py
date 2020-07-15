import tkinter as tk
import time
import shutil, os, zipfile

class Backup():
    NOTIFICATION_TIMEOUT = 5000 # in milliseconds
    BACKUP_INTERVAL = 30 # seconds between backups

    def __init__(self):
        self.job = None
        self.source = None
        self.dest = None
        self.remainingTime = self.BACKUP_INTERVAL * 60

        self.root = tk.Tk()
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.lblSource = tk.Label(text="Source")
        self.lblDestination = tk.Label(text="Destination")
        self.entSource = tk.Entry(width=100)
        self.entDestination = tk.Entry(width=100)
        self.btnBackupInterval = tk.Button(text="Backup 30min", command=self.getEntries)
        self.btnStopBackup = tk.Button(text="Stop", command=self.stopBackup, state=tk.DISABLED)

        self.addWidgetsToWindow()

    def addWidgetsToWindow(self):
        self.lblSource.grid(row=0, column=0)
        self.lblDestination.grid(row=1, column=0)
        self.entSource.grid(row=0, column=1)
        self.entDestination.grid(row=1, column=1)
        self.btnBackupInterval.grid(row=0, column=2)
        self.btnStopBackup.grid(row=1, column=2)

    def getEntries(self):
        self.source = self.entSource.get()
        self.dest = self.entDestination.get()
        self.remainingTime = self.BACKUP_INTERVAL * 60
        self.lblTimeToNextBackup = tk.Label()
        self.lblTimeToNextBackup.grid(row=2, columnspan=3)
        self.createBackup()

    def createBackup(self):
        if self.source == "" or self.dest == "":
            self.showNotification()
            self.btnBackupInterval["state"] = tk.DISABLED
            self.btnStopBackup["state"] = tk.DISABLED
        else:
            self.btnBackupInterval["state"] = tk.DISABLED
            self.btnStopBackup["state"] = tk.NORMAL

            if self.remainingTime > 0:
                self.remainingTime -= 1
            else:
                src = self.source
                os.chdir(self.source)
                os.chdir("..")
                dst = os.getcwd()
                currentTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                sourceFolder = self.source.split("\\")[-1]
                backupFolder = sourceFolder + "_BACKUP"
                if not os.path.exists(os.getcwd() + "\\" + backupFolder):
                    os.makedirs(backupFolder)
                os.chdir(backupFolder)
                destDir = os.getcwd() + "\\" + sourceFolder + "_" + currentTime
                shutil.copytree(self.source, destDir)
                self.remainingTime = self.BACKUP_INTERVAL * 60
        
            self.lblTimeToNextBackup.config(text=f"Next backup in: {int(self.remainingTime / 60)}:{'{:0>2}'.format(self.remainingTime % 60)}")

            self.job = self.root.after(1000, self.createBackup)

    def stopBackup(self):
        self.root.after_cancel(self.job)
        self.btnStopBackup["state"] = tk.DISABLED
        self.btnBackupInterval["state"] = tk.NORMAL
        self.lblTimeToNextBackup.destroy()

    def showNotification(self):
        self.lblNotification = tk.Label(text="Source and destination fields cannot be empty!")
        self.lblNotification.grid(row=2, columnspan=3)
        self.root.after(self.NOTIFICATION_TIMEOUT, self.deleteNotification)

    def deleteNotification(self):
        self.lblNotification.destroy()
        self.btnBackupInterval["state"] = tk.NORMAL


backup = Backup()
