import pf_data, file_decompressor, os, time
from colorama import Fore

class MessageFunctions:
    @staticmethod
    def warning(message):
        print(f"{Fore.YELLOW}[!] {message}{Fore.RESET}")

    @staticmethod
    def error(message):
        print(f"{Fore.RED}[-] {message}{Fore.RESET}")

    @staticmethod
    def info(message):
        print(f"{Fore.CYAN}[i] {message}{Fore.RESET}")

    @staticmethod
    def success(message):
        print(f"{Fore.GREEN}[+] {message}{Fore.RESET}")

MessageFunctions = MessageFunctions()

class Prefetch:
    @staticmethod
    def get_prefetch_data(prefetch_file):
        try:
            prefetchData = pf_data.PrefetchData()
            file_name, file_run_count, file_executed_times, volumes = prefetchData.read_prefetch_file(prefetch_file)
            print(f"{Fore.CYAN}File Name:{Fore.RESET} {Fore.YELLOW}{file_name}")
            print(f"{Fore.CYAN}File Run Count:{Fore.RESET} {Fore.YELLOW}{file_run_count}")

            file_run_count = 0
            print(f"{Fore.GREEN}{'-' * 10}\tLast Executed Times:\t{'-' * 10}{Fore.RESET}")
            for timestamp in file_executed_times:
                file_run_count += 1
                print(f"{Fore.YELLOW}{file_run_count}.Run Time: {Fore.CYAN}{timestamp}{Fore.RESET}")

            print(f"{Fore.GREEN}{'-' * 10}\tVolumes:\t{'-' * 10}{Fore.RESET}")
            for volume in volumes:
                print(f"{Fore.YELLOW}{volume}{Fore.RESET}")

        except FileNotFoundError:
            MessageFunctions.error("File not found!")
            exit()

        except Exception as e:
            MessageFunctions.error(f"An error occurred: {e}")

    @staticmethod
    def read_prefetch_header(prefetch_file):
        if not os.path.exists(prefetch_file):
            MessageFunctions.error("File not found!")
            exit()

        elif not os.path.basename(prefetch_file).endswith(".pf"):
            MessageFunctions.error("File is not a prefetch file!")
            exit()

        with open(prefetch_file, "rb") as file:
            header = file.read(8)

        file.close()

        if header[4:] == B'SCCA':
            os.system('cls' if os.name == 'nt' else 'clear')

            Prefetch.get_prefetch_data(prefetch_file)

        elif header[0:3] == B'MAM':
            os.system('cls' if os.name == 'nt' else 'clear')

            file_decompressor.FileDecompressor(prefetch_file,
                                               prefetch_file[:-3] + "_decompressedFile.pf").decompress_file()
            Prefetch.get_prefetch_data(prefetch_file[:-3] + '_decompressedFile.pf')
            os.remove(prefetch_file[:-3] + '_decompressedFile.pf')

            if not os.path.exists(prefetch_file[:-3] + '_decompressedFile.pf'):
                pass
            else:
                MessageFunctions.warning("Decompressed file was not deleted.")

        else:
            MessageFunctions.error("File is not a prefetch file!")
            exit()

class Main:
    @staticmethod
    def main():
        os.system('cls' if os.name == 'nt' else 'clear')

        prefetch_file = input("Please enter the path of the prefetch file "
                              f"({Fore.CYAN}e.g C:\\Users\\User\\Downloads\\example.pf{Fore.RESET}): ")

        if prefetch_file[0] == '"' and prefetch_file[-1] == '"':
            prefetch_file = prefetch_file[1:-1]

        elif prefetch_file.lower() == "exit" or prefetch_file.lower() == "quit" or prefetch_file.lower() == "q" or prefetch_file.lower() == "e":
            MessageFunctions.info("Goodbye!")
            time.sleep(1)
            exit()

        Prefetch.read_prefetch_header(prefetch_file)

Main.main()
