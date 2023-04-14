import random

feet_in_mile = 5280
meters_in_kms= 1000
movies = ["The Dark Knight","The Batman","Fight Club","John Wick"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1,num)