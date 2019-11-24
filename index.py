# Improting Image class from PIL module 
from PIL import Image
import os

# final variables
rectLENGTH = 87     # dimension(s) for each grid
startLEFT = 89      # first box left coordinates
startTOP = 158      # first box top coordinates
lrINBETWEEN = rectLENGTH + 2     # lrINBETWEEN: # of pixels from top left of prev col to top left of next col     
tbINBETWEEN = rectLENGTH + 31    # tbINBETWEEN: # of pixels from top left of prev row to top left of next row
ROWS = 13
COLS = 12

# cut from sheet an appropriate box
def cut(left, top, sheet):
    right  = left + (rectLENGTH)
    bottom = top  + (rectLENGTH)
    character = sheet.crop((left, top, right, bottom))
    return character

# move on to next character
def moveOn(row, col, left, top):
    if (row == ROWS - 1):
        row = 0
        col += 1

        left = startLEFT
        top = startTOP + col * tbINBETWEEN
        #     158 + col * 118
    else:
        row += 1
        left = startLEFT + row * lrINBETWEEN
        #      89 + row * 89

    return row, col, left, top

def imageBreak(SHEETDIR):
    # Opens a image in RGB mode
    DIR = os.getcwd()
    SHEET = Image.open(os.path.join(DIR, SHEETDIR)) 

    # current variables
    cLeft = startLEFT
    cTop = startTOP
    cRow = 0
    cCol = 0
    num = 0
    imgName = ''
    
    # while statement
    while (cCol < COLS):
        num += 1
        character = cut(cLeft, cTop, SHEET)

        #print(str(num) + ':\n\tRowCol - ' + str((cLeft, cTop)))

        imgName = 'char' + str(num) + '.png'
        imgDir = 'chars\\' + imgName

        character.save(imgDir)

        cRow, cCol, cLeft, cTop = moveOn(cRow, cCol, cLeft, cTop)

    PATH = os.path.join(os.getcwd(), 'chars')
    return PATH

if __name__ == '__main__':
    print(imageBreak('sheetTEST.jpg'))