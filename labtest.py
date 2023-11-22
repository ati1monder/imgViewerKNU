import os
import tkinter as tk
from PIL import Image, ImageTk

class PictureViewer():
    def __init__(self):
        self.dir = ''
    
    def menu(self):
        while True:
            menu_number = int(input('Enter the number to choose what you need:' + '\n' +
                                '1. View picture' + '\n' +
                                '2. Select directory' + '\n' +
                                '3. Exit' + '\n' +
                                'Response: '))
            match menu_number:
                case(1):
                    self.show_picture_test()
                case(2):
                    self.chkExDirectory()
                case(3):
                    break
                case _:
                    os.system('cls')
                    print('You have chosen the wrong number')

    def show_picture_test(self):
        if self.dir == '':
            os.system('cls')
            print("Sorry, but I am unable to open a window withough choosing the folder.")
        else:
            self.show_picture()

    def load_image(self, filename):
        self.image = Image.open(filename)
        self.image = self.image.resize([int(self.image.width/2), int(self.image.height/2)])
        photo = ImageTk.PhotoImage(self.image)
        return photo
    
    def show_picture(self, directory='./'):
        root = tk.Tk()
        root.title("Image Viewer")

        if directory != './':
            self.dir = directory

        self.picture = os.listdir(self.dir)
        self.choiceButton = 0
        
        image_path = self.dir + '/' + self.picture[self.choiceButton]
        self.image = Image.open(image_path)
        self.image = self.image.resize([int(self.image.width/2), int(self.image.height/2)])
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(root, image=self.photo)
        self.label.pack()

        buttonLeft = tk.Button(root, text='Previous', command=lambda: self.choosePicture(0))
        buttonLeft.pack(side=tk.LEFT, anchor=tk.S, padx=50, pady=10)

        buttonRight = tk.Button(root, text='Next', command=lambda: self.choosePicture(1))
        buttonRight.pack(side=tk.RIGHT, anchor=tk.S, padx=50, pady=10)

        root.mainloop()

    def choosePicture(self, buttonChoice):
        if buttonChoice == 0:
            self.choiceButton = (self.choiceButton - 1) % len(self.picture)
        elif buttonChoice == 1:
            self.choiceButton = (self.choiceButton + 1) % len(self.picture)

        self.update_image()

    def update_image(self):
        image_path = self.dir + '/' + self.picture[self.choiceButton]
        self.image = Image.open(image_path)
        self.image = self.image.resize([int(self.image.width/2), int(self.image.height/2)])
        self.photo = ImageTk.PhotoImage(self.image)
        self.label.config(image=self.photo)

    def showPicture(self):
        self.picture = os.listdir(self.dir)
        return self.dir + '/' + self.picture[self.choiceButton]
    
    def saveDirectory(self, location):
        os.system('cls')
        print(self.dir)
        saveDirectoryBool = input('Do you want to save the directory you were in?' + '\n' +
                                  'Yes/No: ')
        if saveDirectoryBool == 'Yes':
            dirw = open('./directory.txt', 'w', encoding='utf-8')
            dirw.write(str(location))

    def chkExDirectory(self):
        if 'directory.txt' in os.listdir('./'):
            file = open('./directory.txt', 'r', encoding='utf-8').read()
            print(file)
            askDir = input('Directory found. Want to use it again?' + '\n' +
                           'Yes/No: ')
            if askDir == 'Yes':
                self.dir = file
            else:
                self.listDirectory()

    def listDirectory(self):
        directory = input('Choose the default directory. If nothing is entered, current folder will be choosen.' + '\n' +
                          'Enter the directory: ')
        if directory == '':
            self.dir = './'
        boolNextDir = input('Do you want to go to the next directory?' + '\n' +
                            'Yes/No: ')
        if boolNextDir == 'Yes':
            self.nextFolder()
        

    def nextFolder(self):
        while True:
            os.system('cls')
            print(self.dir)
            print(str(os.listdir(self.dir)).strip('[').strip(']'))
            listDir = input('Choose the next directory. If you want to stop, just write "endlStop". To go back to the previous folder, write "../"' + '\n' +
                    'Enter the directory: ')
            if listDir == 'endlStop':
                self.saveDirectory(self.dir)
                break
            # elif listDir == '../':
            #     self.dir = self.dir[:self.dir[:-1].rfind('/')+1]
            else:
                self.dir = self.dir + '/' + listDir
            

the = PictureViewer()
the.menu()