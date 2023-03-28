import os
import shutil
import argparse


class ImageBackup:
    def __init__(self, name_string='', image_types=['.jpg', '.jpeg', '.png', '.gif']):
        self.root_dir = os.getcwd()
        self.name_string = name_string
        self.image_types = image_types

    def backup_images(self):
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            bak_dir = os.path.join(dirpath, 'bak')
            if os.path.isdir(bak_dir):
                overwrite = input(f"Directory {bak_dir} already exists. Overwrite? (y/n): ")
                if overwrite.lower() != 'y':
                    continue
                shutil.rmtree(bak_dir)
            os.makedirs(bak_dir)
            for filename in filenames:
                ext = os.path.splitext(filename)[-1].lower()
                if ext in self.image_types and self.name_string in filename:
                    src_path = os.path.join(dirpath, filename)
                    backup_path = os.path.join(bak_dir, filename)
                    shutil.copy2(src_path, backup_path)
                    print(f"Backed up {filename} to {backup_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backup image files that contain a given string in their names.')
    parser.add_argument('-n', '--name', dest='name_string', default='',
                        help='String that should be present in the filenames of the image files to be backed up ('
                             'default: all image files)')
    parser.add_argument('-t', '--types', dest='image_types', nargs='+', default=['.jpg', '.jpeg', '.png', '.gif'],
                        help='List of file extensions for the image files to be backed up (default: .jpg, .jpeg, '
                             '.png, .gif)')
    args = parser.parse_args()

    backup = ImageBackup(args.name_string, args.image_types)
    backup.backup_images()