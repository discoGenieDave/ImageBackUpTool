import os
import shutil
import argparse
import json


#####################################################################
# Usage:
#
# 1 Place script in the root directory that needs to be searched.
# 2. Make sure Python is installed. 
# 3. Open Command Prompt or Terminal 
# 4. type: python texctureBackUpTool.py -n name -t filetype 
# 5. Use the name of the file you are looking for and the type of image 
# 6. A back up dir called bak will be created next to each instance found. 
##########################################################################




class ImageBackup:
    def __init__(self, name_string='', image_types=['.jpg', '.jpeg', '.png', '.gif']):
        self.root_dir = os.getcwd()
        self.name_string = name_string
        self.image_types = image_types
        self.backup_files = []
        self.no_image_dirs = []

def backup_images(self):
    for dirpath, dirnames, filenames in os.walk(self.root_dir):
        if 'bak' in dirnames:
            dirnames.remove('bak')
        bak_dir = os.path.join(dirpath, 'bak')
        if not os.path.isdir(bak_dir):
            os.makedirs(bak_dir)
        backed_up_files = []
        for filename in filenames:
            ext = os.path.splitext(filename)[-1].lower()
            if ext in self.image_types and self.name_string in filename:
                src_path = os.path.join(dirpath, filename)
                backup_path = os.path.join(bak_dir, filename)
                shutil.copy2(src_path, backup_path)
                backed_up_files.append(filename)
                print(f"Backed up {filename}")
        if not backed_up_files:
            self.no_image_dirs.append(dirpath)
        else:
            self.backup_files.append((dirpath, backed_up_files))
    
    self.backup_files = dict(self.backup_files)
    with open('backup_report.json', 'w') as f:
        json.dump({'backup_files': self.backup_files, 'no_image_dirs': self.no_image_dirs}, f, indent=4)


    def write_report(self):
        report = {
            'backup_files': self.backup_files,
            'no_image_dirs': self.no_image_dirs
        }
        with open('backup_report.json', 'w') as f:
            json.dump(report, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backup image files that contain a given string in their names.')
    parser.add_argument('-n', '--name', dest='name_string', default='',
                        help='String that should be present in the filenames of the image files to be backed up (default: all image files)')
    parser.add_argument('-t', '--types', dest='image_types', nargs='+', default=['.jpg', '.jpeg', '.png', '.gif'],
                        help='List of file extensions for the image files to be backed up (default: .jpg, .jpeg, .png, .gif)')
    args = parser.parse_args()

    backup = ImageBackup(args.name_string, args.image_types)
    backup.backup_images()
    backup.write_report()