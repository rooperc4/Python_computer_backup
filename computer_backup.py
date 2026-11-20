
import os
import shutil
import time
import datetime

def incremental_backup(source_dir, backup_dir, last_backup_time):
    # Create a timestamped backup directory
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    dest_dir = os.path.join(backup_dir, f"incremental_backup_{timestamp}")

    with open(last_backup_time, 'r', encoding='utf-8') as file:
        last_backup_time = file.read()
    last_backup_time=float(last_backup_time)
    #last_backup_time=time.strptime(last_backup_time,"%Y-%m-%d_%H:%M:%S")
    #last_backup_time=float(time.mktime(last_backup_time))
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
                 # Check if the file was modified after the last backup
            if os.path.getmtime(file_path) > last_backup_time:
                # Copy only modified files
                dest_file_path = os.path.join(dest_dir, os.path.relpath(file_path, source_dir))
                dest_file_dir = os.path.dirname(dest_file_path)
                if not os.path.exists(dest_file_dir):
                    os.makedirs(dest_file_dir)
                shutil.copy2(file_path, dest_file_path)
                print(f"Copied: {file_path}")

 
    print(f"Incremental backup completed to {dest_dir}")

################################################################
import os
import shutil
import time
import datetime

def new_backup_time(last_backup_time):
    timestamp = time.time()
    with open(last_backup_time, 'w', encoding='utf-8') as file:
        file.write(str(timestamp))  

#################################################################

incremental_backup("C:/Users/rooperc/Desktop","I:/DFOLaptopBackup/IncrementalBackups/Desktop","I:/DFOLaptopBackup/last_backup_time.txt")
incremental_backup("C:/Users/rooperc/Documents/Chris Work Stuff","I:/DFOLaptopBackup/IncrementalBackups/Documents","I:/DFOLaptopBackup/last_backup_time.txt")
incremental_backup("C:/github","I:/DFOLaptopBackup/IncrementalBackups/github","I:/DFOLaptopBackup/last_backup_time.txt")
new_backup_time("I:/DFOLaptopBackup/last_backup_time.txt")


###############################################################

def backup_files(source_dir, backup_dir):
    # Create a timestamped directory for the backup
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_dir = os.path.join(backup_dir, f"backup_{timestamp}")

    # Copy files to the backup directory
    try:
        shutil.copytree(source_dir, dest_dir)
        print(f"Backup completed successfully. Files copied to {dest_dir}")
    except Exception as e:
        print(f"Backup failed: {e}")

source_directory = "/path/to/source"
backup_directory = "/path/to/backup"

#backup_files("C:/Users/rooperc/Desktop","I:/DFOLaptopBackup/Desktop")
#backup_files("C:/Users/rooperc/Documents","I:/DFOLaptopBackup/Documents")
#backup_files("C:/github","I:/github")

