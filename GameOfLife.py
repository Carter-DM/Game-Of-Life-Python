"""
Python implementation of Conway's Game Of Life
GUI created with Tkinter


Code by: Carter Daly-MacPhail
email: cdalymac@gmail.com
10/15/2017

Game of Life algorithm is property of John Horton Conway
"""
from tkinter import *
import random

# creating window
window = Tk()
window.resizable(width=False, height=False)
window.title("Game of Life")


# ===============Change color of cells================
def changeColor(event):
    if(canvas.itemcget(CURRENT, "fill")) == "black":
        canvas.itemconfig(CURRENT, fill="white")
    else:
        canvas.itemconfig(CURRENT, fill="black")

def preset_random():
        for random_c in range(len(cells)):
            color = random.choice([True, False])
            if color == True:
                canvas.itemconfig(cells[random_c], fill="black")
            else:
                canvas.itemconfig(cells[random_c], fill="white")

def preset_glider():
    middle_cell = (len(cells)//2) - (num_of_cells//2)
    canvas.itemconfig(cells[middle_cell-num_of_cells], fill="black")
    canvas.itemconfig(cells[middle_cell+1], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells-1)], fill="black")
    canvas.itemconfig(cells[middle_cell+num_of_cells], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells+1)], fill="black")

def preset_small_exploder():
    middle_cell = (len(cells)//2) - (num_of_cells//2)
    canvas.itemconfig(cells[middle_cell], fill="black")
    canvas.itemconfig(cells[middle_cell-num_of_cells], fill="black")
    canvas.itemconfig(cells[middle_cell-1], fill="black")
    canvas.itemconfig(cells[middle_cell+1], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells-1)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells+1)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells*2)], fill="black")

def preset_exploder():
    middle_cell = (len(cells)//2) - (num_of_cells//2)
    canvas.itemconfig(cells[middle_cell-(num_of_cells*2)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)+2)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-2)], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells+2)], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells-2)], fill="black")
    canvas.itemconfig(cells[middle_cell-2], fill="black")
    canvas.itemconfig(cells[middle_cell+2], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells-2)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells+2)], fill="black")
    canvas.itemconfig(cells[middle_cell+((num_of_cells*2)-2)], fill="black")
    canvas.itemconfig(cells[middle_cell+((num_of_cells*2)+2)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells*2)], fill="black")

def preset_ten_cells():
    middle_cell = (len(cells)//2) - (num_of_cells//2)
    canvas.itemconfig(cells[middle_cell], fill="black")
    canvas.itemconfig(cells[middle_cell-1], fill="black")
    canvas.itemconfig(cells[middle_cell-2], fill="black")
    canvas.itemconfig(cells[middle_cell-3], fill="black")
    canvas.itemconfig(cells[middle_cell-4], fill="black")
    canvas.itemconfig(cells[middle_cell-5], fill="black")
    canvas.itemconfig(cells[middle_cell+1], fill="black")
    canvas.itemconfig(cells[middle_cell+2], fill="black")
    canvas.itemconfig(cells[middle_cell+3], fill="black")
    canvas.itemconfig(cells[middle_cell+4], fill="black")

def preset_glider_gun():
    if num_of_cells > 38:
        middle_cell = (len(cells)//2) - (num_of_cells//2)
        canvas.itemconfig(cells[middle_cell], fill="black")
        canvas.itemconfig(cells[middle_cell-1], fill="black")
        canvas.itemconfig(cells[middle_cell-3], fill="black")
        canvas.itemconfig(cells[middle_cell-(num_of_cells+1)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*2)+2)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*3)+4)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*3)+5)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*2)+6)], fill="black")
        canvas.itemconfig(cells[middle_cell-(num_of_cells+7)], fill="black")
        canvas.itemconfig(cells[middle_cell-(num_of_cells+16)], fill="black")
        canvas.itemconfig(cells[middle_cell-(num_of_cells+17)], fill="black")
        canvas.itemconfig(cells[middle_cell-7], fill="black")
        canvas.itemconfig(cells[middle_cell-16], fill="black")
        canvas.itemconfig(cells[middle_cell-17], fill="black")
        canvas.itemconfig(cells[middle_cell + (num_of_cells - 7)], fill="black")
        canvas.itemconfig(cells[middle_cell+((num_of_cells*2)-6)], fill="black")
        canvas.itemconfig(cells[middle_cell+((num_of_cells*3)-5)], fill="black")
        canvas.itemconfig(cells[middle_cell+((num_of_cells*3)-4)], fill="black")
        canvas.itemconfig(cells[middle_cell+((num_of_cells*2)-2)], fill="black")
        canvas.itemconfig(cells[middle_cell+(num_of_cells-1)], fill="black")
        canvas.itemconfig(cells[middle_cell-(num_of_cells-3)], fill="black")
        canvas.itemconfig(cells[middle_cell-(num_of_cells-4)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-3)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-4)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*3)-3)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*3)-4)], fill="black")
        canvas.itemconfig(cells[middle_cell+5], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*4)-5)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*4)-7)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*5)-7)], fill="black")
        canvas.itemconfig(cells[middle_cell+7], fill="black")
        canvas.itemconfig(cells[middle_cell+(num_of_cells+7)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*3)-17)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-17)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*3)-18)], fill="black")
        canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-18)], fill="black")

def preset_tumbler():
    middle_cell = (len(cells)//2) - (num_of_cells//2)
    canvas.itemconfig(cells[middle_cell-1], fill="black")
    canvas.itemconfig(cells[middle_cell+1], fill="black")
    canvas.itemconfig(cells[middle_cell-3], fill="black")
    canvas.itemconfig(cells[middle_cell+3], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells+1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)+1)], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells-1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)+2)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*3)+1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*3)+2)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-2)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*3)-1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*3)-2)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells-1)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells-3)], fill="black")
    canvas.itemconfig(cells[middle_cell+((num_of_cells*2)-2)], fill="black")
    canvas.itemconfig(cells[middle_cell+((num_of_cells*2)-3)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells+1)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells+3)], fill="black")
    canvas.itemconfig(cells[middle_cell+((num_of_cells*2)+2)], fill="black")
    canvas.itemconfig(cells[middle_cell+((num_of_cells*2)+3)], fill="black")

def preset_light_spaceship():
    middle_cell = (len(cells)//2) - (num_of_cells//2)
    canvas.itemconfig(cells[middle_cell+2], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells+1)], fill="black")
    canvas.itemconfig(cells[middle_cell+(num_of_cells-2)], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells-2)], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells+2)], fill="black")
    canvas.itemconfig(cells[middle_cell-(num_of_cells*2)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)+1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-1)], fill="black")
    canvas.itemconfig(cells[middle_cell-((num_of_cells*2)-2)], fill="black")

def reset_grid():
    for update_cell in range(len(cells)):
        canvas.itemconfig(cells[update_cell], fill="white")


# ========================================================

"""
========================================================
          S I M U L A T I O N  S T A R T
========================================================
"""

# global variable that dictates whether or not the simulation runs
start = False

def start_simulation():

    # clearing old list of colors and setting the new one to the colors currently on screen
    del new_frame[:]
    for cell_colors in range(len(cells)):
            new_frame.append(canvas.itemcget(cells[cell_colors], "fill"))
    global start
    start = True
    simulation()

def stop_simulation():
    # setting the start global variable to false thus stopping the recursive loop in simulation()
    global start
    start = False

def simulation():
    if start:

        '''
        Because of the fact that I'm checking the state of each cell sequentially
        I want to avoid updating the cells as I go because the cells should not affect each other until
        the next frame.
        So I've created a second list where I will store the colors that the cells will change to
        and after the whole canvas is checked and an appropriate color has been selected for each cell,
        then change all the cells' colors at once.
        '''

        # updating the "frame"
        for update_cell_colors in range(len(cells)):
            canvas.itemconfig(cells[update_cell_colors], fill=new_frame[update_cell_colors])

        # looping and checking each cell in the canvas
        for i in range(len(cells)-1):

            cur_color = canvas.itemcget(cells[i], "fill")

            # initialising each neighbor
            n_neighbor = ""
            ne_neighbor = ""
            e_neighbor = ""
            se_neighbor = ""
            s_neighbor = ""
            sw_neighbor = ""
            w_neighbor = ""
            nw_neighbor = ""

            '''
            =====Special Cases for cells along the edges of the canvas====
            '''
            # if cell is on top row
            if i < num_of_cells:
                n_neighbor = "white"
                nw_neighbor = "white"
                ne_neighbor = "white"

            # if cell is in westernmost column
            west_wall = 0
            while west_wall <= (len(cells)):
                if i == west_wall:
                    w_neighbor = "white"
                    nw_neighbor = "white"
                    sw_neighbor = "white"
                west_wall += int(num_of_cells)

            # if cell is in easternmost column
            east_wall = num_of_cells-1
            while east_wall < (len(cells)+1):
                if i == east_wall:
                    e_neighbor = "white"
                    ne_neighbor = "white"
                    se_neighbor = "white"
                east_wall += int(num_of_cells)

            # if cell is in bottom row
            if (i < len(cells)-1) and (i > ((len(cells)-1)-num_of_cells)):
                s_neighbor = "white"
                sw_neighbor = "white"
                se_neighbor = "white"

            '''
            ======C H E C K I N G  S T A T E  O F  N E I G H B O R S======
            '''
            alive_neighbors = 0
            neighbors =[n_neighbor, ne_neighbor, e_neighbor, se_neighbor, s_neighbor, sw_neighbor, w_neighbor, nw_neighbor]
            for check_neighbors in range(len(neighbors)):

                # if the neighbor is still blank then that means it's not beyond one of the edges so check it's state
                if neighbors[check_neighbors] == "":

                    # NORTH NEIGHBOR
                    if check_neighbors == 0:
                        check_color = canvas.itemcget(cells[(i-num_of_cells)], "fill")
                        if check_color == "black":
                            alive_neighbors += 1

                    # NORTH EAST NEIGHBOR
                    elif check_neighbors == 1:
                        check_color = canvas.itemcget(cells[(i-(num_of_cells-1))], "fill")
                        if check_color == "black":
                                alive_neighbors += 1

                    # EASTERN NEIGHBOR
                    elif check_neighbors == 2:
                        check_color = canvas.itemcget(cells[(i+1)], "fill")
                        if check_color == "black":
                                alive_neighbors += 1

                    # SOUTH EAST NEIGHBOR
                    elif check_neighbors == 3:
                        check_color = canvas.itemcget(cells[(i+num_of_cells+1)], "fill")
                        if check_color == "black":
                                alive_neighbors += 1

                    # SOUTH NEIGHBOR
                    elif check_neighbors == 4:
                        check_color = canvas.itemcget(cells[(i+num_of_cells)], "fill")
                        if check_color == "black":
                                alive_neighbors += 1

                    # SOUTH WEST NEIGHBOR
                    elif check_neighbors == 5:
                        check_color = canvas.itemcget(cells[(i+(num_of_cells-1))], "fill")
                        if check_color == "black":
                                alive_neighbors += 1

                    # WEST NEIGHBOR
                    elif check_neighbors == 6:
                        check_color = canvas.itemcget(cells[(i-1)], "fill")
                        if check_color == "black":
                                alive_neighbors += 1

                    # NORTH WEST NEIGHBOR
                    elif check_neighbors == 7:
                        check_color = canvas.itemcget(cells[(i-(num_of_cells+1))], "fill")
                        if check_color == "black":
                                alive_neighbors += 1
            '''
            ========================================================
                          T H E  A L G O R I T H M
            ========================================================
            '''
            if (cur_color == "black") and (alive_neighbors < 2):
                new_frame[i] = "white"

            elif (cur_color == "black") and ((alive_neighbors == 2) or (alive_neighbors == 3)):
                new_frame[i] = "black"

            elif (cur_color == "black") and (alive_neighbors > 3):
                new_frame[i] = "white"

            elif (cur_color == "white") and (alive_neighbors == 3):
                new_frame[i] = "black"

        # recursively call simulation after certain milliseconds
        canvas.after(speed_slider.get(), simulation)
'''
========================================================
             S I M U L A T I O N  E N D
========================================================
'''

'''
========================================================
                 G U I  W I D G E T S   
========================================================
'''

# window dimensions variable is both x and y values for main window
window_dimensions = 600

'''
@NOTE: num_of_cells divisor MUST divide EVENLY into window_dimensions
'''
num_of_cells = int(window_dimensions / 15)

canvas = Canvas(window, width=window_dimensions, height=window_dimensions)
canvas.grid(row=0, rowspan=20, column=0, columnspan=2)

'''
=====Buttons and Labels=====
'''
start_button = Button(window, text="Start Simulation", bg="#b0efa5", command=start_simulation)
start_button.grid(row=21, column=0)

stop_button = Button(window, text="Stop Simulation", bg="#eda7a1", command=stop_simulation)
stop_button.grid(row=21, column=1)

preset_frame = Frame(window, width=(window_dimensions//4), height=(window_dimensions//2), bg="#e0e0e0")
preset_frame.grid(row=0, column=3)

speed_frame = Frame(window, width=(window_dimensions//4), height=(window_dimensions//2),bg="#e0e0e0")
speed_frame.grid(row=1, column=3)

label1 = Label(preset_frame, width=(window_dimensions//32), text="Presets", bg="#e0e0e0", font=("Calibri", 16, "bold"))
label1.grid(row=0, column=0, columnspan=2,pady=5)

label2 = Label(speed_frame, text="Speed", bg="#e0e0e0", font=("Calibri", 16, "bold"))
label2.grid(row=0, column=0, columnspan=2, pady=5)

label3 = Label(speed_frame, text="(In milliseconds)", bg="#e0e0e0")
label3.grid(row=1, column=0, columnspan=2, pady=5)

label4 = Label(speed_frame, width=(window_dimensions//16), text="\nPython implementation of \nConway's Game Of Life.\nGUI created with Tkinter\n\n\
Code by: Carter Daly-MacPhail\nemail: cdalymac@gmail.com\n10/15/2017\n\n\
Game of Life algorithm is property \nof John Horton Conway", font=("Calibri", 8))
label4.grid(row=3, column=0, columnspan=2)

speed_slider = Scale(speed_frame, from_=10, to=1000, orient=HORIZONTAL)
speed_slider.grid(row=2, column=0, columnspan=2, padx=(50), pady=(25))

random_button = Button(preset_frame, text="Random", command=preset_random)
random_button.grid(row=1, column=0, columnspan=2, pady=15)

glider_button = Button(preset_frame, text="Glider", command=preset_glider)
glider_button.grid(row=2, column=0, padx=5, pady=5)

sm_exploder_button = Button(preset_frame, text="Small Exploder", command=preset_small_exploder)
sm_exploder_button.grid(row=2, column=1, padx=5, pady=5)

exploder_button = Button(preset_frame, text="Exploder", command=preset_exploder)
exploder_button.grid(row=3, column=0, padx=5, pady=5)

ten_cell_button = Button(preset_frame, text="10 Cell Row", command=preset_ten_cells)
ten_cell_button.grid(row=3, column=1, padx=5, pady=5)

glider_gun_button = Button(preset_frame, text="Gosper Glider Gun", command=preset_glider_gun)
glider_gun_button.grid(row=4, column=0, padx=5, pady=5)

tumbler_button = Button(preset_frame, text="Tumbler", command=preset_tumbler)
tumbler_button.grid(row=4, column=1, padx=5, pady=5)

light_spaceship_button = Button(preset_frame, text="Lightweight Spaceship", command=preset_light_spaceship)
light_spaceship_button.grid(row=5, column=0,  columnspan=2, padx=5, pady=5)

reset_button = Button(preset_frame, text="Reset Grid", bg="#eda7a1", command=reset_grid)
reset_button.grid(row=6, column=0, columnspan=2, padx=5, pady=15)

'''
========================================================
       P R I N T I N G  I N I T I A L  G R I D
========================================================
'''

y = 0
x = 0
# Creating list of cells for easy access later
cells = []
# Creating list of cells' colors
new_frame = []

# iterate through each row, creating cells along the way
while y < window_dimensions:
    while x < window_dimensions:

        # create each individual cell and initially set each's color to white
        item = canvas.create_rectangle(x, y, (x + (window_dimensions/num_of_cells)), (y + (window_dimensions/num_of_cells)), fill="white", outline="#a3a3a3")

        # adding each cell to the cell list
        cells.append(item)

        # increase x coordinate by width of cell
        x = int(x + (window_dimensions / num_of_cells))

    # reset x value to zero because we're moving down a row
    x = 0
    # increase y value by 1 because we're moving down a row
    y = int(y + (window_dimensions / num_of_cells))


# CHECK FOR CLICKS
canvas.bind("<Button-1>", changeColor)

# calling simulation loop
simulation()

window.mainloop()
