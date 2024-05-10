import winreg, os, socket, sqlite3
from colorama import Fore

class Functions:
    def __init__(self):
        self.errorFile = "errors.txt"

    def get_regedit(self, hkey, regedit_key, file_name):
        try:
            key = winreg.OpenKey(hkey, regedit_key)
            try:
                with open(file_name, "w") as regeditFile:
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            regeditFile.write(f"{name} : {value}\n")
                            i += 1
                        except WindowsError:
                            break
            except Exception as e:
                with open(self.errorFile, "a") as errorFile:
                    errorFile.write(f"{e}\n")
        except Exception as e:
            with open(self.errorFile, "a") as errorFile:
                errorFile.write(f"{e}\n")

    def get_location(self, location, file_name):
        try:
            files = os.listdir(location)

            with open(file_name, "w") as amacheFile:
                for file in files:
                    file_path = os.path.join(location, file)
                    with open(file_path, "r") as current_file:
                        file_content = current_file.read()
                        amacheFile.write(f"--------------------- {file} ---------------------\n{file_content}\n")
        except Exception as e:
            with open(self.errorFile, "a") as errorFile:
                errorFile.write(f"{e}\n")

            errorFile.close()

Functions = Functions()
class Application_Execution:
    def Shimcache(self):
        hkey = winreg.HKEY_LOCAL_MACHINE
        regedit_key = r"SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache"
        Functions.get_regedit(hkey, regedit_key, "Shimcache.txt")

    def Task_Bar_Feature_Usage(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_key = r"NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\FeatureUsage"
        Functions.get_regedit(hkey, regedit_key, "Task_Bar_Feature_Usage.txt")

    def Amache(self):
        location = r"C:\Windows\appcompat\Programs\Amcache.hve"
        Functions.get_location(location, "Amache.txt")

    def Jump_Lists(self):
        pass

    def Last_Visited_MRU(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_key = r"NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU"
        Functions.get_regedit(hkey, regedit_key, "MRU.txt")

    def Commands_Executed_in_the_Run_Dialog(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_key = r"NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU"
        Functions.get_regedit(hkey, regedit_key, "Commands_Executed_in_the_Run_Dialog.txt")

    def Windows10_Timeline(self):
        try:
            profile = os.getlogin()
            account_id = f"L.{os.getlogin()}"
            target_directory = f"C:\\Users\\{profile}\\AppData\\Local\\ConnectedDevicesPlatform\\{account_id}\\ActivitiesCache.db"

            conn = sqlite3.connect(target_directory, timeout=10)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            with open("Windows_Timeline.txt", "w") as TimelineFile:
                for table in tables:
                    table_name = table[0]
                    TimelineFile.write(str(f"--------------------- {table_name} ---------------------\n"))
                    cursor.execute(f"SELECT * FROM {table_name};")
                    rows = cursor.fetchall()

                    for row in rows:
                        TimelineFile.write(str(row))
                        TimelineFile.write("\n")

                    TimelineFile.write("\n")

            conn.close()
        except sqlite3.Error as sqlite_error:
            print(f"{Fore.RED}Sqlite hatası! {sqlite_error}{Fore.RESET}")

        except Exception as e:
            print(f"{Fore.RED}Error! {e}{Fore.RESET}")

    def BAMDAM(self):
        # regedit_key kontrol edilecek
        hkey = winreg.HKEY_LOCAL_MACHINE
        regedit_key = r"SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\{SID}"
        Functions.get_regedit(hkey, regedit_key, "BAMDAM.txt")

    def SRUM(self):
        location = r"C:\Windows\System32\sru"
        Functions.get_location(location, "SRUM.txt")

    def Prefetch(self):
        location = r"C:\Windows\Prefetch"
        regedit_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters"
        Functions.get_location(location, "Prefetch.txt")
        pass

    def CapabilityAccessManager(self):
        hkey = winreg.HKEY_LOCAL_MACHINE
        hkey_ = winreg.HKEY_CURRENT_USER
        regedit_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore"
        regedit_path_ = r"NTUSER\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore"
        Functions.get_regedit(hkey, regedit_path, "CapabilityAccessManager.txt")
        Functions.get_regedit(hkey_, regedit_path_, "CapabilityAccessManager2.txt")

    def UserAssist(self):
        # GUID bakılacak
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count"
        pass

class File_and_Folder_Opening:
    def OpenSaveMRU(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePIDlMRU"
        Functions.get_regedit(hkey, regedit_path, "OpenSaveMRU.txt")

    def RecentFiles(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs"
        Functions.get_regedit(hkey, regedit_path, "RecentFiles.txt")

    def MS_Word_Reading_Locations(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER\Software\Microsoft\Offi ce\<Version>\Word\Reading Locations"
        Functions.get_regedit(hkey, regedit_path, "MS_Word_Reading_Locations.txt")

    def Last_Visited_MRU(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU"
        Functions.get_regedit(hkey, regedit_path, "Last_Visited_MRU.txt")

    def Shorcut_Files(self):
        pass

    def OfficeRecentFiles(self):
        hkey = winreg.HKEY_CURRENT_USER
        hkey_ = winreg.HKEY_CURRENT_USER
        hkey__ = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Offi ce\<Version>\<AppName>\File MRU"
        regedit_path_ = r"NTUSER.DAT\Software\Microsoft\Offi ce\<Version>\<AppName>\User MRU\LiveId_####\File MRU"
        regedit_path__ = r"NTUSER.DAT\Software\Microsoft\Offi ce\<Version>\<AppName>\User MRU\AD_####\File MRU"
        Functions.get_regedit(hkey, regedit_path, "OfficeRecentFiles.txt")
        Functions.get_regedit(hkey_, regedit_path_, "OfficeRecentFiles2.txt")
        Functions.get_regedit(hkey__, regedit_path__, "OfficeRecentFiles3.txt")

    def ShellBags(self):
        hkey = winreg.HKEY_CURRENT_USER
        hkey_ = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU"
        regedit_path_ = r"NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags"
        Functions.get_regedit(hkey, regedit_path, "ShellBags.txt")
        Functions.get_regedit(hkey_, regedit_path_, "ShellBags2.txt")

    def JumpLists(self):
        pass

    def OfficeTrustRecords(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER\Software\Microsoft\Office\<Version>\<AppName>\Security\Trusted Documents\TrustRecords"
        Functions.get_regedit(hkey, regedit_path, "OfficeTrustRecords.txt")

    def OfficeOAlerts(self):
        pass

    def InternetExplorerFile(self):
        pass

class Deleted_Items_and_File_Existence:
    def ThumbsDB(self):
        pass

    def WindowsSearchDatabase(self):
        location = r"C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb"
        location_ = r"C:\ProgramData\Microsoft\Search\Data\Applications\Windows\GatherLogs\SystemIndex"
        Functions.get_location(location, "WindowsSearchDatabase.txt")
        Functions.get_location(location_, "WindowsSearchDatabase2.txt")

    def InternetExplorerFile(self):
        pass

    def SearchWordWheelQuery(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery"
        Functions.get_regedit(hkey, regedit_path, "SearchWordWheelQuery.txt")

    def UserTypedPaths(self):
        hkey = winreg.HKEY_CURRENT_USER
        regedit_path = r"NTUSER\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths"
        Functions.get_regedit(hkey, regedit_path, "UserTypedPaths.txt")

    def Thumbcache(self):
        pass

    def RecycleBin(self):
        location = r"C:\$Recycle.Bin"
        Functions.get_location(location, "Recycle.txt")

class Browser_Activity:
    def HistoryAndDownloadHistory(self):
        pass

    def MediaHistory(self):
        pass

    def HTML5WebStorage(self):
        pass

    def HTML5FileSystem(self):
        pass

    def AutoCompleteData(self):
        pass

    def Browser_Preferences(self):
        pass

    def Cache(self):
        pass

    def Bookmarks(self):
        pass

    def Stored_Credentials(self):
        pass

    def Browser_Downloads(self):
        pass

    def Extensions(self):
        pass

    def Session_Restore(self):
        pass

    def Cookies(self):
        pass

class CloudStorage:
    def OneDrive(self):
        pass

    def Google_Drive_for_Desktop(self):
        pass

    def Box_Drive(self):
        pass

    def Dropbox(self):
        pass

class Account_Usage:
    def Cloud_Account_Details(self):
        pass

    def Last_Login_and_Password_Change(self):
        pass

    def Service_Events(self):
        pass

    def User_Accounts(self):
        pass

    def RDP(self):
        pass

    def SuccessfulFailedLogons(self):
        pass

    def Authentication_Events(self):
        pass

    def Logon_Event_Types(self):
        pass

class Network_Activity_and_Physical_Location:
    def Network_History(self):
        pass

    def Browser_URL_Parameters(self):
        pass

    def Timezone(self):
        pass

    def WLAN_Evet_Log(self):
        pass

    def Network_Interfaces(self):
        pass

    def SRUM(self):
        pass

class External_Device_USB_Usage:
    def USB_Device_Identification(self):
        pass

    def Event_Logs(self):
        pass

    def Drive_Letter_and_Volume_Name(self):
        pass

    def User_Information(self):
        pass

    def ShortcutFiles(self):
        pass

    def Connection_Timestamps(self):
        pass

    def VSN(self):
        pass

class SystemInformation:
    def Windows_Defender(self):
        try:
            target_directory = r"C:\ProgramData\Microsoft\Windows Defender\Support"

            files = os.listdir(target_directory)

            with open("Windows_Defender.txt", "w") as WindowsDefender:
                for file in files:
                    file_path = os.path.join(target_directory, file)
                    with open(file_path, "r") as current_file:
                        file_content = current_file.read()
                        WindowsDefender.write(f"--------------------- {file} ---------------------\n{file_content}\n")

        except Exception as e:
            with open("defenderError.txt", "w") as defenderErrFile:
                defenderErrFile.write(f"Error! : {e}")

    def Operating_System_Version(self):
        pass

    def ComputerName(self):
        try:
            print(f"Computer Name: {socket.gethostname()}")
        except Exception as e:
            print(f"{Fore.RED}Error! {e}{Fore.RESET}")

    def System_Boot_Autostart_Programs(self):
        pass

    def System_Last_Shutdown_Time(self):
        pass

class Start:
    def StartAll(self):
        application_Execution = Application_Execution()
        application_Execution.Shimcache()
        application_Execution.Task_Bar_Feature_Usage()
        application_Execution.Amache()
        application_Execution.Jump_Lists()
        application_Execution.Last_Visited_MRU()
        application_Execution.Commands_Executed_in_the_Run_Dialog()
        application_Execution.Windows10_Timeline()
        application_Execution.BAMDAM()
        application_Execution.SRUM()
        application_Execution.Prefetch()
        application_Execution.CapabilityAccessManager()
        application_Execution.UserAssist()
        # Application Execution Sonu
        # .................................
        file_and_Folder_Opening = File_and_Folder_Opening()
        file_and_Folder_Opening.OpenSaveMRU()
        file_and_Folder_Opening.RecentFiles()
        file_and_Folder_Opening.MS_Word_Reading_Locations()
        file_and_Folder_Opening.Last_Visited_MRU()
        file_and_Folder_Opening.Shorcut_Files()
        file_and_Folder_Opening.OfficeRecentFiles()
        file_and_Folder_Opening.ShellBags()
        file_and_Folder_Opening.JumpLists()
        file_and_Folder_Opening.OfficeTrustRecords()
        file_and_Folder_Opening.OfficeOAlerts()
        file_and_Folder_Opening.InternetExplorerFile()
        # File and Folder Opening Sonu
        # .................................
        deleted_Items_and_File_Existence = Deleted_Items_and_File_Existence()
        deleted_Items_and_File_Existence.ThumbsDB()
        deleted_Items_and_File_Existence.WindowsSearchDatabase()
        deleted_Items_and_File_Existence.InternetExplorerFile()
        deleted_Items_and_File_Existence.SearchWordWheelQuery()
        deleted_Items_and_File_Existence.UserTypedPaths()
        deleted_Items_and_File_Existence.Thumbcache()
        deleted_Items_and_File_Existence.RecycleBin()
        # Deleted Items and File Existence Sonu
        # .................................
        browser_activity = Browser_Activity()
        browser_activity.HistoryAndDownloadHistory()
        browser_activity.MediaHistory()
        browser_activity.HTML5WebStorage()
        browser_activity.HTML5FileSystem()
        browser_activity.AutoCompleteData()
        browser_activity.Browser_Preferences()
        browser_activity.Cache()
        browser_activity.Bookmarks()
        browser_activity.Stored_Credentials()
        browser_activity.Browser_Downloads()
        browser_activity.Extensions()
        browser_activity.Session_Restore()
        browser_activity.Cookies()
        # Browser Activity Sonu
        # .................................
        cloudStorage = CloudStorage()
        cloudStorage.OneDrive()
        cloudStorage.Google_Drive_for_Desktop()
        cloudStorage.Box_Drive()
        cloudStorage.Dropbox()
        # CloudStorage Sonu
        # .................................
        account_Usage = Account_Usage()
        account_Usage.Cloud_Account_Details()
        account_Usage.Last_Login_and_Password_Change()
        account_Usage.Service_Events()
        account_Usage.User_Accounts()
        account_Usage.RDP()
        account_Usage.SuccessfulFailedLogons()
        account_Usage.Authentication_Events()
        account_Usage.Logon_Event_Types()
        # Account Usage
        # .................................
        network_Activity_and_Physical_Location = Network_Activity_and_Physical_Location()
        network_Activity_and_Physical_Location.Network_History()
        network_Activity_and_Physical_Location.Browser_URL_Parameters()
        network_Activity_and_Physical_Location.Timezone()
        network_Activity_and_Physical_Location.WLAN_Evet_Log()
        network_Activity_and_Physical_Location.Network_Interfaces()
        network_Activity_and_Physical_Location.SRUM()
        # Network Activity and Physical Location Sonu
        # .................................
        external_Device_USB_Usage = External_Device_USB_Usage()
        external_Device_USB_Usage.USB_Device_Identification()
        external_Device_USB_Usage.Event_Logs()
        external_Device_USB_Usage.Drive_Letter_and_Volume_Name()
        external_Device_USB_Usage.User_Information()
        external_Device_USB_Usage.ShortcutFiles()
        external_Device_USB_Usage.Connection_Timestamps()
        external_Device_USB_Usage.VSN()
        # External Device USB Usage Sonu
        # .................................
        systemInformation = SystemInformation()
        systemInformation.Windows_Defender()
        systemInformation.Operating_System_Version()
        systemInformation.ComputerName()
        systemInformation.System_Boot_Autostart_Programs()
        systemInformation.System_Last_Shutdown_Time()
        # System Information Sonu