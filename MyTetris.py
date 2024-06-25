# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:04:22 2023

@author: jakov
"""

from tkinter import Tk, Frame, Label, Canvas
from PIL import Image, ImageTk
import random
from Pieces import LongPiece, LPiece, SquigglyLPiece, SquarePiece, TPiece, ReverseLPiece, SquigglyReverseLPiece
from time import sleep


class Tetris():
    
    def __init__(self):
        self.root = Tk()
        
        self.ws = int(self.root.winfo_screenwidth()) # width of the screen
        
        self.game_speed = 100
        self.was_init_placed = False
        self.first_piece_placed = False
        
        self.init_pieces()
        
        self.init_board()
        

        self.root.mainloop()            


    def init_board(self):
        self.box_size = 40
        self.pad_size = 1
        self.main_width = (self.box_size+2*self.pad_size)*10
        
        self.main_game_frame = Frame(self.root, width=self.main_width, 
                                     height=2*self.main_width, 
                                     background="light blue")
        
        self.root_geometry = f"{str(int(1.5*self.main_width))}x{str(2*self.main_width)}"
        self.root.geometry(self.root_geometry + "+580+0")
        
        self.main_game_frame.grid_propagate(False)
        self.main_game_frame.pack(side="left")
        self.root.bind("<Key>", self.key_pressed)
        
        self.main_info_frame = Frame(self.root, width=self.main_width/2, 
                                     height=2*self.main_width, 
                                     background="light blue")
        self.main_info_frame.pack(side="right")

        self.main_list = self.init_main_list()
        
        self.label = Label(self.main_info_frame)
    
        self.init_main_placement()

        
    def init_main_list(self):
        lst = []
        self.frame_lst = []
        
        for i in range(20):
            lst.append([])
            self.frame_lst.append([])

        for i in range(20):
            for j in range(10):
                lst[i].append(0)
                self.frame_lst[i].append(Frame(self.main_game_frame, background="medium aquamarine",
                      width=self.box_size, height=self.box_size))
                self.frame_lst[i][j].grid(row=i,column=j,padx=1,pady=1)
                
        return lst
    
    
    def init_pieces(self):
        self.long_piece = LongPiece()
        self.l_piece = LPiece()
        self.squiggly_l_piece = SquigglyLPiece()
        self.square_piece = SquarePiece()
        self.t_piece = TPiece()
        self.reverse_l_piece = ReverseLPiece()
        self.squiggly_reverse_l_piece = SquigglyReverseLPiece()

        
    
    def update_board(self, updates):
        for coord in updates:
            if (coord[2] == "add"):
                self.frame_lst[coord[0]][coord[1]].config(background="red")
            else:
                self.frame_lst[coord[0]][coord[1]].config(background="medium aquamarine")
    
    
    def update_cleared_board(self):
        for row in range(20):
            for column in range(10):
                if (self.main_list[row][column] == 1):
                    self.frame_lst[row][column].config(background="red")
                else:
                    self.frame_lst[row][column].config(background="medium aquamarine")
                
                
    def key_pressed(self, event):
        if self.was_init_placed:
            if (event.char == "1" or event.char == "3"):
                self.data = self.piece.move(self.main_list, event.char)
                self.main_list = self.data[0]
                self.update_board(self.data[2])
                
            elif (event.char == "z" or event.char == "x"):
                self.data = self.piece.rotate(self.main_list, event.char)
                self.main_list = self.data[0]
                self.update_board(self.data[2])
            
        else:
            print(event.char)          
            
            
    def place_random_piece(self):
        """Create random piece and place it.
        
        Possible pieces:
            0: Long bar
            1: L piece
            2: L squigly
            3: Reverse L piece
            4: Reverse L squigly
            5: T piece
            6: Square
        """
        self.label.destroy()
        
        if not self.first_piece_placed:
            piece = random.randint(0,6)
            self.first_piece_placed = True
        else:
            piece = self.piece2
        self.piece2 = random.randint(0,6)


        if piece == 0:
            self.piece = self.long_piece
        elif piece == 1:
            self.piece = self.l_piece
        elif piece == 2:
            self.piece = self.squiggly_l_piece
        elif piece == 3:
            self.piece = self.reverse_l_piece
        elif piece == 4:
            self.piece = self.squiggly_reverse_l_piece
        elif piece == 5:
            self.piece = self.t_piece
        else:
            self.piece = self.square_piece
            
            
        if self.piece2 == 0:
            self.image = Image.open("LongPiece.png")
        elif self.piece2 == 1:
            self.image = Image.open("LPiece.png")
        elif self.piece2 == 2:
            self.image = Image.open("SquigglyLPiece.png")
        elif self.piece2 == 3:
            self.image = Image.open("ReverseLPiece.png")
        elif self.piece2 == 4:
            self.image = Image.open("ReverseSquigglyLPiece.png")
        elif self.piece2 == 5:
            self.image = Image.open("TPiece.png")
        else:
            self.image = Image.open("SquarePiece.png")
        
        photo = ImageTk.PhotoImage(self.image.resize((196, 98), Image.ANTIALIAS))

        self.label = Label(self.main_info_frame, image=photo, bg='green')
        self.label.image = photo
        self.label.pack()
        self.image.close()
        
    
    def init_main_placement(self):
        self.place_random_piece()
        self.data = self.piece.init_placement(self.main_list)
        self.main_list = self.data[0]
        self.update_board(self.data[2])
        self.was_init_placed = True
        self.main_game_frame.after(self.game_speed, self.main_loop)
        
        
    def clear_rows(self):
        interval = self.piece.get_y_interval()
        n_updates = 0
        for row in interval:
            if sum(self.main_list[row]) == 10:
                self.main_list[1:row+1] = self.main_list[0:row]
                self.main_list[0] = [0,0,0,0,0,0,0,0,0,0]
                n_updates += 1

        if n_updates > 0:
            self.update_cleared_board()
            self.game_speed -= n_updates*2
            
            
    def reset_game(self):
        self.piece.reset()
        self.main_list = self.init_main_list()
        self.update_cleared_board()
        self.init_main_placement()
    
        
    def main_loop(self):
        self.data = self.piece.check_drop_ability(self.main_list)
        self.main_list = self.data[0]
        
        if (self.data[1] == "NotPlaced"):
            self.update_board(self.data[2])
            self.main_game_frame.after(self.game_speed, self.main_loop)
            
        elif (self.data[1] == "InPlace"):
            self.was_init_placed = False
            self.clear_rows()
            self.piece.reset()
            self.main_game_frame.after(self.game_speed, self.init_main_placement)
            
        elif (self.data[1] == "UnableToPlace"):
            self.reset_game()

    
Tetris()



