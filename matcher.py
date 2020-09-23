import glob
import shutil, os

cwd = os.getcwd()
'''
folder path :
	xml path
	image path
	create matching_files folder
file format :
	In this example i used png if you are having jpg formats means you can change all png to jpg and use
'''

cwd_xml 	= cwd + "\\" + "xml\\"
cwd_frames  = cwd + '\\' + 'images\\'
pathC = cwd + '\\matching_files\\'
len_xml = len(cwd_xml)
len_frames = len(cwd_frames)
a1 = '.png'
count = 1

files_xml = [f for f in glob.glob(cwd_xml + "**/*.xml", recursive=True)]
files_frames = [f for f in glob.glob(cwd_frames + "**/*.png", recursive=True)]

'''
find the file names with same name and copy the matched filels to matching_files 
'''
# copying png 
# copy the same xml name png files to matching_files folder
for f in files_xml:

	f = f[len_xml:]
	f = f[:-3]
	f = f + 'png'
	
	print(count)
	count += 1
	for f1 in files_frames:
		f1 = f1[len_frames:]
		if f == f1 :
			f1 = cwd_frames + '\\' + f1
			shutil.copy(f1, pathC)

# copying xml
# copy the same png name xml files to matching_files folder			
for f in files_frames:
	f = f[len_frames:]
	f = f.split(".")[0]
	f = f+".xml"
	
	
	for f1 in files_xml:
		f1 = f1[len_xml:]
		if f == f1:
			f1 = cwd_xml + '\\' + f1
			shutil.copy(f1, pathC)
 
print("_________________________________________________________________________________")


'''
if you want to perform any one of this task means you can just command that and use.
'''