# FTP
import ftplib


def ftp_connect():  # Connect to the FTP and start asking for commands
    while True:  # If connection fails, retry
        site_address = input('Enter FTP address: ')
        try:

            with ftplib.FTP(site_address) as ftp:
                ftp.login()
                print(ftp.getwelcome())
                print('Directory Listing for', ftp.pwd())
                ftp.dir()
                print('Valid commands are cd/get/exit - ex: get readme.txt')
                ftp_command(ftp)
                break  # once ftp_command() exits, end this function (exit program)
        except ftplib.all_errors as e:  # treat all exceptions at this point as a connection failure
            print('Failed to connect, check your address.', e)


def ftp_command(ftp):
    while True:  # Run until 'exit' command is received from user
        command = input('Enter a command: ')  # get next command from user
        commands = command.split()  # split command and file/directory into list
        if commands[0] == 'cd':  # Change directory
            try:
                ftp.cwd(commands[1])
                print('Directory listing for', ftp.pwd())
                ftp.dir()
                print('Current Directory', ftp.pwd())
            except ftplib.error_perm as e:  # Handle 550 (not found / no permission error)
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'Directory may not exist or you may not have permission to view it.')
        elif commands[0] == 'get':  # Download file
            try:
                ftp.retrbinary('RETR ' + commands[1], open(commands[1], 'wb').write)
                print('File successfully downloaded.')
            except ftplib.error_perm as e: # Handle 550 (not found / no permission error)
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'File may not exist or you may not have permission to view it.')
        elif commands[0] == 'ls':  # Print directory listing
            print('Directory listing for', ftp.pwd())
            ftp.dir()
        elif commands[0] == 'exit':  # Exit application
            ftp.quit()
            print('Goodbye.')
            break
        else:
            print('Invalid command, try again (valid options: cd/get/exit).')


print("Welcome to Python FTP!")
ftp_connect()
