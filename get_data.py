import winreg, os, socket, sqlite3
from colorama import Fore

class Functions:
    def read_registry_key(self, key, subkey):
        try:
            with winreg.OpenKey(key, subkey) as reg_key:
                subkey_count, value_count, _ = winreg.QueryInfoKey(reg_key)

                subkeys = []
                for i in range(subkey_count):
                    subkeys.append(winreg.EnumKey(reg_key, i))

                # Get values
                values = {}
                for i in range(value_count):
                    value_name, value_data, value_type = winreg.EnumValue(reg_key, i)
                    values[value_name] = value_data

                return subkeys, values
        except FileNotFoundError:
            print("Registry key not found.")
            return None, None
        except Exception as e:
            print(f"Error! {e}")
            return None, None

class Application_Execution:
    def Shimcache(self):
        pass

    def Task_Bar_Feature_Usage(self):
        pass

    def Amache(self):
        pass

    def Jump_Lists(self):
        pass

    def Last_Visited_MRU(self):
        pass

    def Commands_Executed_in_the_Run_Dialog(self):
        pass

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
        pass

    def SRUM(self):
        pass

    def Prefetch(self):
        pass

    def CapabilityAccessManager(self):
        pass

    def UserAssist(self):
        pass

class File_and_Folder_Opening:
    def OpenSaveMRU(self):
        pass

    def RecentFiles(self):
        pass

    def MS_Word_Reading_Locations(self):
        pass

    def Last_Visited_MRU(self):
        pass

    def Shorcut_Files(self):
        pass

    def OfficeRecentFiles(self):
        pass

    def ShellBags(self):
        pass

    def JumpLists(self):
        pass

    def OfficeTrustRecords(self):
        pass

    def OfficeOAlerts(self):
        pass

    def InternetExplorerFile(self):
        pass

class Deleted_Items_and_File_Existence:
    def ThumbsDB(self):
        pass

    def WindowsSearchDatabase(self):
        pass

    def InternetExplorerFile(self):
        pass

    def SearchWordWheelQuery(self):
        pass

    def UserTypedPaths(self):
        pass

    def Thumbcache(self):
        pass

    def RecycleBin(self):
        pass

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

            with open(f"{target_directory}\\MPDetection-20240419-192123.log", "r") as MPDetection:
                DefenderDetection = MPDetection.read()

            MPDetection.close()

            with open(f"{target_directory}\\MPDeviceControl-20240419-221710.log", "r") as MPDeviceControl:
                DefenderDeviceControl = MPDeviceControl.read()

                MPDeviceControl.close()

            with open(f"{target_directory}\\MPLog-20240419-192123.log", "r") as MPLog:
                DefenderLog = MPLog.read()

            MPLog.close()

            with open(f"{target_directory}\\MPScanSkip-20240420-132450.log", "r") as MPScanSkip:
                DefenderScanSkip = MPScanSkip.read()

            MPScanSkip.close()

            with open("Windows_Defender.txt", "w") as WindowsDefender:
                WindowsDefender.write(
                    str(f"--------------------- Defender Detection ---------------------\n{DefenderDetection}\n--------------------- Defender Device Control ---------------------\n{DefenderDeviceControl}\n--------------------- Defender Log ---------------------\n{DefenderLog}\n--------------------- Defender Scan Skip ---------------------\n{DefenderScanSkip}"))
            WindowsDefender.close()

        except Exception as e:
            print(f"Error! {e}")

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