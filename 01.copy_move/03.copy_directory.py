from distutils.dir_util import copy_tree

from_directory = "source_folder"
to_directory = "big_folder"

copy_tree(from_directory, to_directory)
# all the contents (including directories) in the source_folder will be copied
# to the destination folder
print 'Copied all data successfully!'
