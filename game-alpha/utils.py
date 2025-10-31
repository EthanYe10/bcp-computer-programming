import pygame as pg
from os import path
from settings import *

class Map:
    # initialize map object from text file
    def __init__(self, filename):
        # data is list of strings
        self.data = []

        # load map from file, using 'with' to ensure file is closed after reading
        with open(filename, "rt") as f:

            # read each line from the file, strip whitespace, and append to data list
            for line in f:
                self.data.append(line.strip())

            # set map dimensions based on data
            # dimensions are 32 pixels per tile
            self.tilewidth = len(self.data[0])
            self.tileheight = len(self.data)
            self.width = self.tilewidth * 32
            self.height = self.tileheight * 32