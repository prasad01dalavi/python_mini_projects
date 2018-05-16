import shutil

source_file_path = "source_folder\\source_file.txt"
# absolute_path = "C:\Users\Prasad\Desktop\python_mini\01.copy_move\01.copy_move_file.py"
# relative_path = "source_folder"

destination_file_path = "destination_folder"

shutil.move(source_file_path, destination_file_path)
print 'Moved the file from source_folder to destination_folder!'


"""
---------------------------------------------------------------------------
| Function          |Copies Metadata|Copies Permissions|Can Specify Buffer|
---------------------------------------------------------------------------
| shutil.copy       |      No       |        Yes       |        No        |
---------------------------------------------------------------------------
| shutil.copyfile   |      No       |         No       |        No        |
---------------------------------------------------------------------------
| shutil.copy2      |     Yes       |        Yes       |        No        |
---------------------------------------------------------------------------
| shutil.copyfileobj|      No       |         No       |       Yes        |
---------------------------------------------------------------------------
"""
