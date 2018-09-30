#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 19:41:21 2018

@author: abdulbasit
"""

from tkinter import font
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
 
img = Image.new('RGB', (40, 40), color = (255, 255, 255))
 


for family in font.families():
    print(family)
    fnt = ImageFont.truetype("Tahoma.ttf", 30)
    d = ImageDraw.Draw(img)
    d.text((0,0), "H", font=fnt, fill=(0, 0, 0))
    #img.save('pil_text.png')
    #img.show()
