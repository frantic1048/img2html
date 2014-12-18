#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## @package img2html.py.py
#  Usage        : img2html.py file1 [file2 ...]
#  Description  : generate a html use box-shadow to show pictures
#  Dependencies : Python Image Library, Python 3
#  Note         : Take care of the Super-High-Energy output ( >﹏<。)
#  Date         : 2014-12-18
#  Author       : frantic1048


import sys
import os
from PIL import Image
from string import Template

## @var docTmpl template for constructing entire html document
docTmpl = Template('''
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>~ ${name} ~</title>
</head>
<body>
  <style type="text/css">${css}</style>
  <div id="image_kun"></div>
</body>
</html>''')

## @var cssTmplStatic template for constructing static image's css code
cssTmplStatic = Template('''
@charset "utf-8";
body{
  display:flex;
  justify-content:center;
  align-items:center;
}
#image_kun{
  height: ${height}px;
  width: ${width}px;
  position:relative;
}
#image_kun::after{
  position:absolute;
  height:1px;
  width:1px;
  background:${firstPixel};
  margin:0;
  padding:0;
  content:"\\200B";/*ZWS*/
  box-shadow:
  ${boxshadow};
}
''')

## @var cssTmplAnimation template for constructing image sequence's css animation code
cssTmplAnimation = Template('''
@charset "utf-8";
body{
  display:flex;
  justify-content:center;
  align-items:center;
}
#image_kun{
  height: ${height}px;
  width: ${width}px;
  position:relative;
}
#image_kun::after{
  position:absolute;
  height:1px;
  width:1px;
  background:transparent;
  margin:0;
  padding:0;
  content:"\\200B";/*ZWS*/
  animation:ayaya ${animationLength} step infinite;
}
@keyframes ayaya{
${animationKeyFrames}
}
  ''')

## write str to a file,named as <exportFileName>.html
def toFile (str,exportFileName):
  with open (exportFileName,'w') as html:
    html.write(str)

## construct HEX Color value for a pixel
#  @param pixel a pixel object to be converted
#  @return hex format color of the pixel
def toHexColor (pixel):
  return '#{0:02x}{1:02x}{2:02x}'.format(*pixel[:])

## construct single box-shadow param
#  @param color valid CSS color
def toBoxShadowParam (x, y, color):
  return format('%spx %spx 0 %s'%(x, y, color))

## process single image file to html
#  @param fileName input file's name
#  @param export output callback(doc, exportFileName):
#    doc : generated html string
#    exportFileName : output filename
def mipaStatic(fileName,export=''):
  with Image.open(fileName) as im:
    ## what called magic
    boxshadow = ''

    ## file name as sysname
    exportFileName = fileName+'.html'
    title = os.path.split(fileName)[-1]

    ## image size
    width, height = im.size[0], im.size[1]

    #ensure RGB mode
    if (im.mode != 'RGB'):
      im = im.convert(mode = 'RGB')

    firstPixel = toHexColor(im.getpixel((0,0)))
    for y in range(0, height):
      for x in range(0, width):
        color = toHexColor(im.getpixel((x, y)))
        #link magic
        boxshadow += toBoxShadowParam(x, y, color)

        #add a spliter if not the end
        if (not (y == height-1 and x == width-1)):
          #keep a '\n' for text editor ˊ_>ˋ
          boxshadow += ',' + '\n'

    doc = docTmpl.substitute(name = title, css = cssTmplStatic.substitute(width = width, height = height, boxshadow = boxshadow, firstPixel=firstPixel))
    if (export==''):
      print(doc)
    else:
      export(doc, exportFileName)

## process a image folder
#  files in folder will processed to an animation
#  process order is filename asend
#  @param fileName input file's name
#  @param export output callback, call with generated html as a string argument
def mipaAnimation(fileName,export=print):
  print('constructing...')

for path in sys.argv[1:]:
  if os.path.isfile(path):
    ##export to stdout
    #mipaStatic(path)

    ##export to autonamed file
    mipaStatic(path,toFile)
  elif os.path.isdir(path):
    mipaAnimation(path)
    #mipaAnimation(path,toFile)
