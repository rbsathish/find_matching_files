# find_matching_files

        Find the same file name present are not if present means copying that files to matching_files folder 
        This will be helpful for dataset preparation in deep learning or you can just use for other purpose also.


matcher.py

        In matcher.py file first you need to give the folder paths where you want to find matching files.

        Here i used to find the matching names for xml files in one folder and png images in other folder.
        (you can change png to jpg if your images is jpg means)

        If same name matches in both folder means i just copy the matched xml and png files to matching_files.
        (if you want to copy the png only means you can comment the xml saving part or if you want copy the xml means you can comment the png part) 
