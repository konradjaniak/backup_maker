import tkinter as tk
import time

class Backup():
    NOTIFICATION_TIMEOUT = 5000 # in milliseconds
    BACKUP_INTERVAL = 5 # seconds between backups

    def __init__(self):
        self.job = None
        self.source = None
        self.dest = None

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
        self.lblTimeToNextBackup = tk.Label()

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
        self.createBackup()

    def createBackup(self):
        if self.source == "" or self.dest == "":
            self.showNotification()
            self.btnBackupInterval["state"] = tk.DISABLED
            self.btnStopBackup["state"] = tk.DISABLED
        else:
            self.btnBackupInterval["state"] = tk.DISABLED
            self.btnStopBackup["state"] = tk.NORMAL
            nextBackup = time.time() + self.BACKUP_INTERVAL
            nextHours = time.gmtime(nextBackup).tm_hour + 2
            nextMinutes = time.gmtime(nextBackup).tm_min
            nextSeconds = time.gmtime(nextBackup).tm_sec
            self.lblTimeToNextBackup.grid(row=2, columnspan=3)
            self.lblTimeToNextBackup.config(text=f"Next backup at: {nextHours}:{nextMinutes}:{nextSeconds}")
            now = time.strftime("%H:%M:%S")
            print("Backup done at: ", now)
            self.job = self.root.after(self.BACKUP_INTERVAL * 1000, self.createBackup)

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
