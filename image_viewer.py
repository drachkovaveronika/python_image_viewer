"""
Image viewer on Python and Tkinter. 
All images come from open sources
"""
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/vaggi/PycharmProjects/project1/icon.ico')
root.geometry("626x710")

my_img1 = ImageTk.PhotoImage(Image.open("flower1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("flower2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("flower3.jpg"))

image_list = [my_img1, my_img2, my_img3]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def next(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_next = Button(root, text=">>", command=lambda: next(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_next = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, anchor=E)
    status.grid(row=2, column=0, columnspan=3, padx=50, pady=10, sticky=W + E)


def back(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_next = Button(root, text=">>", command=lambda: next(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, anchor=E)
    status.grid(row=2, column=0, columnspan=3, padx=50, pady=10, sticky=W + E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="exit", command=root.quit)
button_next = Button(root, text=">>", command=lambda: next(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, padx=50, pady=10, sticky=W + E)

root.mainloop()
