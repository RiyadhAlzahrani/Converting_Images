#only img is supported in the script
import os
from posixpath import splitext
from PIL import Image

from_format, to_format = input("from format? "), input("to format? ")

#finding the path to get the img
base_path = str(os.getcwd() +'\\Base\\')

if not os.path.exists(base_path):
    os.mkdir(base_path)
print("")
print(base_path)
input("Move the files to the folder \"Base\", then Press Enter to continue...")

#finding the path or creating it to store the img
to_path = str(os.getcwd() +'\\' + to_format.upper() +'\\')

#create a list file names
in_file_list = os.listdir(base_path)

if in_file_list.__len__() >= 1 :
    #get evrey file in the file list
    for in_file_name in in_file_list:

        in_file_path = os.path.join(base_path, in_file_name)
        #check the input file is exest in the base file
        if os.path.isfile(in_file_path):
            #split the path to "\\\" and ".ext"
            f, e = os.path.splitext((base_path + in_file_name))
            #check the file if its the wanted extintion 
            if e == ("."+from_format.lower()):

                #n name the file and m is the extention
                n, m = splitext(in_file_name)

                if not os.path.exists(to_path):
                    os.mkdir(to_path)
                
                #create output name with extention and the path
                out_file_name = n + "."+to_format.lower()
                out_file_path = os.path.join(to_path, out_file_name)

                #check if the file is not allrady converted 
                if not os.path.isfile(out_file_path):
                    #open and save as the wanted format
                    im = Image.open(in_file_path)
                    im.save(out_file_path)
                else:
                    print(out_file_name+" is alrady converted")
        else:
            print(in_file_path+" is not exist")
else:
    print("error")
print("Script ended")
