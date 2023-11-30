# from tkinter import *
# from random import randint
# from tkinter import ttk

# root = Tk()
# root.title("Rock-Paper-Scissors game")
# root.geometry("500x600")
# root.config(bg="lightblue")

# rock = PhotoImage(file=r"C:\Users\NEW\Desktop\Eze_Tkinter_Projects\images\rock.png")
# paper = PhotoImage(file=r"C:\Users\NEW\Desktop\Eze_Tkinter_Projects\images\paper.png")
# scissors = PhotoImage(file=r"C:\Users\NEW\Desktop\Eze_Tkinter_Projects\images\scissors.png")

# objects = [rock, paper, scissors]
# number_selector = randint(0,2)

# image_label = Label(root,image= objects[number_selector])
# image_label.pack(pady= 0)

# user_choice = ttk.Combobox(root, value = ["rock", "paper", "scissors"])
# user_choice.pack(padx= 50, pady= 50)


# def spin():
#     selected_index = user_choice.current() 
#     number_selector = randint(0,2)
#     image_label.config(image= objects[number_selector])
#     #0 = Rock
#     #1 = Paper
#     #2 = Scissors
#     if number_selector == 0 and  selected_index == 0:
#         win_lose.config(text="It's a Draw!!")
#     if number_selector == 0 and  selected_index == 1:
#         win_lose.config(text="You win!!")
#     if number_selector == 0 and  selected_index == 2:
#         win_lose.config(text="You Lose!!")

#     if number_selector == 1 and  selected_index == 0:
#        win_lose.config(text="You Lose!!")
#     if number_selector == 1 and  selected_index == 1:
#          win_lose.config(text="It's a Draw!!")
#     if number_selector == 1 and  selected_index == 2:
#         win_lose.config(text="You win!!")

#     if number_selector == 2 and  selected_index == 0:
#          win_lose.config(text="You win!!")
#     if number_selector == 2 and  selected_index == 1:
#           win_lose.config(text="You Lose!!")
#     if number_selector == 2 and  selected_index == 2:
#         win_lose.config(text="It's a Draw!!")

# win_lose = Label(root, text= "", font = "Helvetica") #Label to show if you won or not
# spin_button = Button(root, text="Spin!", command = lambda: spin())
# spin_button.pack(padx= 50, pady= 50)
# win_lose.pack()

# root.mainloop()
