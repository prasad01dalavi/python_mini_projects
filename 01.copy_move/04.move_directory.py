import shutil

source_directory = "source_folder"

destination_directory = "big_folder_1"

shutil.move(source_directory, destination_directory)
print 'Moved the file from source_folder to destination_folder!'
