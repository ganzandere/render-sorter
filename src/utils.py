import os
import shutil
import sys

if __name__ == '__main__':
    raw_dir_path = input("\nPlease copy RenderLayer directory path and press 'Enter': \n")
    dir_path = raw_dir_path.replace("\\", "/") + "/"
    if not os.path.isdir(dir_path):
        sys.exit("Please enter a valid directory path!\n")

    render_layer = input("\nPlease input RenderLayer name including a version and press 'Enter': \n (Example: sc0600_layout_v03) \n" )
    if (len(render_layer) < 2):
        sys.exit("Please enter a valid render layer name!\n")
    files = os.listdir(dir_path)

    count = 0
    miss = 0
    for file in files:
        if count > 5:
            break
        if render_layer not in file:
            miss += 1
        count += 1

    if miss > 2:
        sys.exit("Please enter a valid render layer name!\n")


    for file in files:
        cut_file = file.replace(render_layer, "")[1:]
        dbg = cut_file.split(".")
        if len(dbg) > 2:
            channel_layer = cut_file.split(".")[0]
            new_folder = dir_path + channel_layer
            old_filepath = dir_path + file
            new_filepath = new_folder + "/" + file
            if not os.path.isdir(new_folder):
                os.mkdir(new_folder)
                print("New folder created: " + new_folder)
            if shutil.move(old_filepath, new_filepath):
                print("Moved file to: " + new_filepath)
