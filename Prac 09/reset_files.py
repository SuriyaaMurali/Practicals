"""
CP1404/CP5632 Practical 9
Reset files to original state
"""

import os
import shutil

DIRECTORY = 'FilesToSort'


def main():
    os.chdir(DIRECTORY)
    folders = get_folders()
    files = get_files('.')

    if not folders:
        print("No folders found!")
    else:
        for folder in folders:
            files += get_files(str(folder))

        move_files()

        for folder in folders:
            os.rmdir(folder)

        print("\nReset complete!")


def get_folders():
    folders = []
    for foldername in os.listdir('.'):
        if os.path.isdir(foldername):
            folders.append(foldername)
    return folders


def get_files(directory):
    files = []
    for filename in os.listdir(directory):
        if not os.path.isdir(filename):
            files.append(filename)
    return files


def move_files():
    for folder in get_folders():
        print("\nFOLDER:", folder)
        os.chdir(folder)
        for file in os.listdir('.'):
            print(file)
            shutil.move(file, '..')
        os.chdir('..')


main()
