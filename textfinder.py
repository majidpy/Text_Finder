import sys
import os
import re


def main():

    # giving folders and files in a given directory
    def directory_expander(init_dir):
        all_dir = os.listdir(init_dir)
        folders_found = []
        files_found = []
        for item in all_dir:
            if os.path.isdir(os.path.join(init_dir, item)):
                folders_found.append(os.path.join(init_dir, item))
            elif os.path.isfile(os.path.join(init_dir, item)):
                files_found.append(os.path.join(init_dir, item))
        return folders_found, files_found

    # opening a file and looking for the text inside or the file name itself
    def text_finder(f_name):
        try:
            head, tail = os.path.split(f_name)
            if tail.split('.')[0] == text_2_find:
                print('This file has the name that you are looking for:', f_name)
        except:
            pass
        try:

            with open(os.path.join(base_dir, f_name), 'r') as f:
                data = f.read()
                search_re = re.findall(text_2_find, data)
                if search_re:
                    print("File \n", f_name, '\n',
                          'has the words {} that you are looking'. format({search_re[0]}))
        except:
            pass

    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    text_2_find = sys.argv[1]

    try:
        folders, files = directory_expander(base_dir)
        while len(folders) > 0:
            interim_folders = []
            for folder in folders:
                folder_dir = os.path.abspath(folder)
                inter_folders, inter_files = directory_expander(folder_dir)
                if inter_folders:
                    interim_folders += inter_folders
                if inter_files:
                    files += inter_files
            folders = interim_folders

        # now, we have all files in the root directory
        for file in files:
            text_finder(file)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
