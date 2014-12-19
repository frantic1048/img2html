#img2html

You want to use html to show your image ?

generate html uses box-shadow to show picture.

Or a html shows your image sequence in a folder as **animation** !

Take care of the Super-High-Energy output ( >﹏<。)

#Usage

`img2html.py file1|dir1 [file2|dir2 ...]`

#Note

To directory, img2html will convert the pictures in the given directory to animation,frame order is asend order of filename.Make sure all the pictures in a image sequence directory are in **same** width and height.

for example(input a directory shows below):

    my_sequence
    ├── 1.jpg
    ├── c.jpg
    ├── o.jpg
    ├── 2.jpg
    ├── 3.jpg
    └── z.jpg
    
the converted frame order is like this (files will be automaticly sorted according to it's name)

    1.jpg --> 2.jpg --> 3.jpg --> c.jpg --> o.jpg --> z.jpg

#Dependencies

- Python 3
- Python Image Library or Pillow
