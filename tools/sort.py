import tkinter
from PIL import ImageTk,Image
import glob
import os

root = tkinter.Tk()
root.title('Image labelling utility')

class ImageSort:
    image = None
    name = None

    def __init__(self):
        try:
            os.mkdir('on')
            os.mkdir('off')
            os.mkdir('discard')
        except FileExistsError:
            pass

    def set_image(self, image):
        self.image = image
        self.name = os.path.basename(image)

    def lights_on(self, event):
        print('lights on: ' + str(self.image))
        self.move('on')
        event.widget.quit()

    def lights_off(self, event):
        print('lights off: ' + str(self.image))
        self.move('off')
        event.widget.quit()

    def discard(self, event):
        print('discard: ' + str(self.image))
        self.move('discard')
        event.widget.quit()

    def move(self, directory):
        try:
            os.rename(self.image, os.path.join(directory, self.name))
        except FileExistsError:
            print('file exists')


sort = ImageSort()

root.bind('y', sort.lights_on)
root.bind('n', sort.lights_off)
root.bind('d', sort.discard)

images = glob.glob('police/*')

for image in images:
    print("sorting: " + image)
    sort.set_image(image)
    display = Image.open(image)
    tk_image = ImageTk.PhotoImage(display)
    width = display.size[0]
    height = display.size[1]
    root.geometry('{}x{}+100+100'.format(width, height))
    image_widget = tkinter.Label(root, image=tk_image)
    image_widget.place(x=0, y=0, width=width, height=height)

    root.mainloop()
