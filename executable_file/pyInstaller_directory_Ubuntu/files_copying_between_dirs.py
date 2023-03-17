# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import os
# from multiprocessing import Pool
import shutil


# from distutils.dir_util import copy_tree

# def test_function():

def directory_copying_detailed(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        item_with_path = os.path.join(src, item)

        if os.path.isdir(item_with_path):
            directory_copying_with_duplicates_preserving(item_with_path, dst, symlinks, ignore)
        else: # checking if file with this name already exists.
            if not os.path.isfile(os.path.join(dst, item)):
                shutil.copy2(item_with_path, dst)
            else: # If file with this name already exists create new file with changed name
                new_file_name = os.path.join(dst, item_with_path, "1")
                shutil.copy2(item_with_path, new_file_name)


def directory_copying_with_duplicates_overwriting_extended(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def directory_copying_with_duplicates_overwriting(src, dst, symlinks=False, ignore=None):
    shutil.copytree(src, dst, dirs_exist_ok=True)
    # shutil.copytree('baz', 'foo', dirs_exist_ok=True)
    # copy subdirectory example
    # from_directory = "a"
    # to_directory = "x"

    # copy_tree(from_directory, to_directory)


def directory_copying_with_duplicates_preserving(src, dst, symlinks=False, ignore=None):
    # if destination folder doesn't exist yet then create it
    print_hi('info1')
    if not os.path.exists(dst):
        os.mkdir(dst)

    print_hi('info2')
    # Walk through all files in the directory that contains the files to be copied
    for root, dirs, files in os.walk(src):
        print_hi('info3')
        print(files)
        print_hi('info4')
        for file in files:
            # use absolute path, in case of need to move several dirs
            file_with_src_path = os.path.join(os.path.abspath(root), file) # src is the same as root
            file_with_dst_path = os.path.join(os.path.abspath(dst), file)

            # If file to be copied does not exist in destination folder
            # then we can simply copy it and continue to next file
            if not os.path.isfile(file_with_dst_path):
                print(file_with_dst_path, ": not found")
                shutil.copy(file_with_src_path, file_with_dst_path)
                continue # skip to the nex file
            print_hi('info5')

            # if file with the same name already exists in destination folder
            # then copy this file to the destination folder with incremented suffix in its name

            # Separate file name base from extension
            filename, extension = os.path.splitext(file)

            # Initial new name of file to be copied
            # new_filename_with_dst_path = os.path.join(dst, filename, extension)

            # if not os.path.exists(new_filename_with_dst_path):  # folder exists, file does not
            #     shutil.copy(file_with_src_path, new_filename_with_dst_path)
            # else:  # folder exists, file exists as well
            index = 1
            while True:
                print_hi('info6')

                new_filename_with_dst_path = os.path.join(dst, filename +"_" + str(index) + extension)
                if not os.path.isfile(new_filename_with_dst_path):
                    shutil.copy(file_with_src_path, new_filename_with_dst_path)
                    print("Copied", file_with_src_path, "as", new_filename_with_dst_path)
                    break
                index += 1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(os.name)
    # print(os.ctermid())
    print(os.environ)
    src_dir = os.getcwd()  # get the current working dir
    print(src_dir)
    print(os.listdir(src_dir))
    print('cmd entry:', sys.argv)

    if len(sys.argv) != 3:
        print("Python script should have 2 arguments - "
              "source folder and destination folder "
              "for copying the files")
        exit(1)

    if not os.path.isdir(sys.argv[1]):
        print("cannot find in operating system the source folder "
              "given as absolute path as first script argument ")
        exit(2)

    # directory_copying_with_duplicates_overwriting('bar', 'foo')
    # directory_copying_with_duplicates_overwriting('baz', 'foo')
    # directory_copying_with_duplicates_overwriting_extended('bar', 'foo')
    # directory_copying_with_duplicates_overwriting_extended('baz', 'foo')
    # directory_copying_detailed('baz', 'foo')
    # directory_copying_with_duplicates_preserving('baz', 'foo')
    # directory_copying_with_duplicates_preserving('bar', 'foo')
    # print(os.listdir('foo'))
    directory_copying_with_duplicates_preserving(sys.argv[1], sys.argv[2])
    print(os.listdir(sys.argv[2]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
