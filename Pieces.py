# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:32:41 2023

@author: jakov
"""

class LongPiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 1
        self.cur_x = 4
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        """This function is called at the start of the game or when a piece has
        been placed.
        
        
        """
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x-1] == 0 and 
            main_list[self.cur_y][self.cur_x] == 0 and
            main_list[self.cur_y][self.cur_x+1] == 0 and 
            main_list[self.cur_y][self.cur_x+2] == 0):

            main_list[self.cur_y][self.cur_x-1] = 1
            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y][self.cur_x+1] = 1
            main_list[self.cur_y][self.cur_x+2] = 1
            
            if (main_list[1][3] == 1 or main_list[1][4] == 1 or
                main_list[1][5] == 1 or main_list[1][6] == 1):
                self.status = "UnableToPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[0,3,"add"],[0,4,"add"],
                                         [0,5,"add"],[0,6,"add"]]]
                
        
    
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        

        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []

        if (self.rotation == 0):
            # When cur_y = 17 the piece is at the bottom. If cur_y <= 16, we
            # check whether it can be moved down. If not, set status = InPlace
            
            if self.cur_y == 17:
                self.status = "InPlace"
                
            else:
                if main_list[self.cur_y+3][self.cur_x] == 1:
                    self.status = "InPlace"
                
                else:
                    main_list[self.cur_y+3][self.cur_x] = 1
                    main_list[self.cur_y-1][self.cur_x] = 0
                
                    updates = [[self.cur_y+3,self.cur_x,"add"],
                               [self.cur_y-1,self.cur_x,"sub"]]
                    self.cur_y += 1

        
        else:
            # Rotation = 1
            if (self.cur_y == 19):
                self.status = "InPlace"
                
            elif (main_list[self.cur_y+1][self.cur_x-1] == 0 and 
                  main_list[self.cur_y+1][self.cur_x] == 0 and
                  main_list[self.cur_y+1][self.cur_x+1] == 0 and 
                  main_list[self.cur_y+1][self.cur_x+2] == 0):
                
                main_list[self.cur_y+1][self.cur_x-1] = 1
                main_list[self.cur_y+1][self.cur_x] = 1
                main_list[self.cur_y+1][self.cur_x+1] = 1
                main_list[self.cur_y+1][self.cur_x+2] = 1
                
                main_list[self.cur_y][self.cur_x-1] = 0
                main_list[self.cur_y][self.cur_x] = 0
                main_list[self.cur_y][self.cur_x+1] = 0
                main_list[self.cur_y][self.cur_x+2] = 0
                
                updates = [[self.cur_y+1, self.cur_x-1, "add"],
                           [self.cur_y+1, self.cur_x, "add"],
                           [self.cur_y+1, self.cur_x+1, "add"],
                           [self.cur_y+1, self.cur_x+2, "add"],
                           [self.cur_y, self.cur_x-1, "sub"],
                           [self.cur_y, self.cur_x, "sub"],
                           [self.cur_y, self.cur_x+1, "sub"],
                           [self.cur_y, self.cur_x+2, "sub"]]
                self.cur_y += 1
                
            else:
                self.status = "InPlace"
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        if (self.rotation == 0):
            if char == "1":
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0 and
                    main_list[self.cur_y+2][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1 
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    main_list[self.cur_y+2][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+2,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"],
                               [self.cur_y+2,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            else:
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0 and
                    main_list[self.cur_y+2][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1 
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    main_list[self.cur_y+2][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    main_list[self.cur_y+2][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y+2,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"],
                               [self.cur_y+2,self.cur_x,"sub"]]
                    
                    self.cur_x += 1
            
            return [main_list, 0, updates]
        
        else:
            #Rotation = 1
            if char == "1":
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x-2] == 0):
                
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y][self.cur_x+2] = 0 
                    
                    updates = [[self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y,self.cur_x+2,"sub"]]
                    self.cur_x -= 1
            else:
                if (self.cur_x == 7):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+3] == 0):
                
                    main_list[self.cur_y][self.cur_x+3] = 1
                    main_list[self.cur_y][self.cur_x-1] = 0 

                    
                    updates = [[self.cur_y,self.cur_x+3,"add"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    
                    self.cur_x += 1
            
            return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        updates = []
        
        if self.rotation == 0:
            if (self.cur_x <= 1 or self.cur_x == 9):
                return [main_list, 0, []]
            
            elif (main_list[self.cur_y][self.cur_x-2] == 0 and
                main_list[self.cur_y][self.cur_x-1] == 0 and
                main_list[self.cur_y][self.cur_x] == 1 and
                main_list[self.cur_y][self.cur_x+1] == 0):
            
                main_list[self.cur_y][self.cur_x-2] = 1
                main_list[self.cur_y][self.cur_x-1] = 1
                main_list[self.cur_y][self.cur_x+1] = 1
                
                main_list[self.cur_y-1][self.cur_x] = 0
                main_list[self.cur_y+1][self.cur_x] = 0
                main_list[self.cur_y+2][self.cur_x] = 0
                
                updates = [[self.cur_y,self.cur_x-2,"add"],
                           [self.cur_y,self.cur_x-1,"add"],
                           [self.cur_y,self.cur_x+1,"add"],
                           [self.cur_y-1,self.cur_x,"sub"],
                           [self.cur_y+1,self.cur_x,"sub"],
                           [self.cur_y+2,self.cur_x,"sub"]]
                self.cur_x -= 1
                self.rotation = 1
                
        else:
            if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                main_list[self.cur_y][self.cur_x+1] == 1 and
                main_list[self.cur_y+1][self.cur_x+1] == 0 and
                main_list[self.cur_y+2][self.cur_x+1] == 0):
            
                main_list[self.cur_y-1][self.cur_x+1] = 1
                main_list[self.cur_y+1][self.cur_x+1] = 1
                main_list[self.cur_y+2][self.cur_x+1] = 1
                
                main_list[self.cur_y][self.cur_x-1] = 0
                main_list[self.cur_y][self.cur_x] = 0
                main_list[self.cur_y][self.cur_x+2] = 0
                
                updates = [[self.cur_y-1,self.cur_x+1,"add"],
                           [self.cur_y+1,self.cur_x+1,"add"],
                           [self.cur_y+2,self.cur_x+1,"add"],
                           [self.cur_y,self.cur_x-1,"sub"],
                           [self.cur_y,self.cur_x,"sub"],
                           [self.cur_y,self.cur_x+2,"sub"]]
                self.cur_x += 1
                self.rotation = 0

        return [main_list, 0, updates]
    
    
    def get_y_interval(self):
        if self.rotation == 0:
            return [self.cur_y-1, self.cur_y, self.cur_y+1, self.cur_y+2]
        else:
            return [self.cur_y]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 1
        self.cur_x = 4
        self.cur_y = 0
        self.status = "NotPlaced"










class LPiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x-1] == 0 and 
            main_list[self.cur_y][self.cur_x] == 0 and
            main_list[self.cur_y][self.cur_x+1] == 0 and 
            main_list[self.cur_y+1][self.cur_x-1] == 0):

            main_list[self.cur_y][self.cur_x-1] = 1
            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y][self.cur_x+1] = 1
            main_list[self.cur_y+1][self.cur_x-1] = 1
            
            if (main_list[2][4] == 1 or main_list[1][5] == 1 or
                main_list[1][6] == 1):
                self.status = "UnableToPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[0,4,"add"],[0,5,"add"],
                                         [0,6,"add"],[1,4,"add"]]]
                
        
        
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        
        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []

        if (self.rotation == 0):
            if self.cur_y == 18:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x] == 1 or 
                    main_list[self.cur_y+1][self.cur_x+1] == 1 or
                    main_list[self.cur_y+2][self.cur_x-1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y+2,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        
        elif (self.rotation == 1):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                
                if (main_list[self.cur_y][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+2][self.cur_x] == 1):
                    self.status = "InPlace"
                else:
                
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y, self.cur_x-1, "add"],
                               [self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y-1, self.cur_x-1, "sub"]]
                    self.cur_y += 1
        
        
        if (self.rotation == 2):
            if self.cur_y == 19:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+1][self.cur_x] == 1 or
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y-1,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        
        elif (self.rotation == 3):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                
                if (main_list[self.cur_y+2][self.cur_x] == 1 or 
                    main_list[self.cur_y+2][self.cur_x+1] == 1):
                    self.status = "InPlace"
                else:
                
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y+2, self.cur_x+1, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y+1, self.cur_x+1, "sub"]]
                    self.cur_y += 1
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        # Rotation = 0
        if (self.rotation == 0):
            # Move piece left
            if char == "1":
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x-2] == 0 and
                    main_list[self.cur_y+1][self.cur_x-2] == 0):
                
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y+1][self.cur_x-2] = 1 
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y+1,self.cur_x-2,"add"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x-1,"sub"]]
                    self.cur_x -= 1
            else:
                # Move piece right
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x] == 0):
                
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1 
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y+1,self.cur_x-1,"sub"]]
                    
                    self.cur_x += 1
            
            return [main_list, 0, updates]
        
        # Rotation = 1
        elif (self.rotation == 1):
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-2] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-2] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-2,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
        
        # Rotation = 2
        elif (self.rotation == 2):
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x] == 0 and
                    main_list[self.cur_y][self.cur_x-2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x] = 1
                    main_list[self.cur_y][self.cur_x-2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+2] == 0 and
                    main_list[self.cur_y][self.cur_x+2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+2] = 1
                    main_list[self.cur_y][self.cur_x+2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x-1] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+2,"add"],
                               [self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
        
        # Rotation = 3
        elif (self.rotation == 3):
            # Rotation = 1
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x+2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        updates = []
        
        # Rotation anti-clockwise
        if (char == "z"):
            # Rotate from 0 to 3
            if (self.rotation == 0):
                if (self.cur_y == 18):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+2][self.cur_x-1] == 0 and
                    main_list[self.cur_y+2][self.cur_x-2] == 0 and
                    main_list[self.cur_y+2][self.cur_x-1] == 0):
                
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+2,self.cur_x,"add"],
                               [self.cur_y+2,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
                    self.cur_x -= 1
                    self.rotation = 3
                    
            # Rotate from 1 to 0
            elif (self.rotation == 1):
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y-1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y-1][self.cur_x+1] = 1

                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_y -= 1
                    self.rotation = 0
                    
            # Rotate from 2 to 1
            elif (self.rotation == 2):
                if (self.cur_y == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-2][self.cur_x] == 0 and
                    main_list[self.cur_y-2][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-2][self.cur_x] = 1
                    main_list[self.cur_y-2][self.cur_x+1] = 1

                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    
                    updates = [[self.cur_y-2,self.cur_x,"add"],
                               [self.cur_y-2,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"]]
                    self.cur_y -= 1
                    self.cur_x += 1
                    self.rotation = 1
                    
            # Rotate from 3 to 2
            elif (self.rotation == 3):
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1

                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"]]
                    self.cur_y += 1
                    self.rotation = 2
                    
        # Rotation clockwise
        else:
            # Rotate from 0 to 1
            if (self.rotation == 0):
                if (self.cur_y == 18):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+1][self.cur_x] == 0 and
                    main_list[self.cur_y+2][self.cur_x] == 0):
                
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+2,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
                    self.rotation = 1
                    
            # Rotate from 1 to 2
            elif (self.rotation == 1):
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+1][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-2] == 0):
                
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-2] = 1

                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y-1,self.cur_x-1,"sub"]]
                    self.cur_y += 1
                    self.cur_x -= 1
                    self.rotation = 2
                    
            # Rotate from 2 to 3
            elif (self.rotation == 2):
                if (self.cur_y == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-2][self.cur_x] == 0 and
                    main_list[self.cur_y-1][self.cur_x] == 0):
                
                    main_list[self.cur_y-2][self.cur_x] = 1
                    main_list[self.cur_y-1][self.cur_x] = 1

                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y-2,self.cur_x,"add"],
                               [self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    self.cur_y -= 1
                    self.rotation = 3
            
            # Rotate from 3 to 0
            elif (self.rotation == 3):
                
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y-1][self.cur_x+2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y-1][self.cur_x+2] = 1
                    
                    main_list[self.cur_y+1][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_y -= 1
                    self.cur_x += 1
                    self.rotation = 0
            
                    
        return [main_list, 0, updates]
    
    
    def get_y_interval(self):
        if self.rotation == 0:
            return [self.cur_y, self.cur_y+1]
        elif self.rotation == 2:
            return [self.cur_y-1, self.cur_y]
        else:
            return [self.cur_y-1, self.cur_y, self.cur_y+1]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"










class SquigglyLPiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x+1] == 0 and 
            main_list[self.cur_y][self.cur_x] == 0 and
            main_list[self.cur_y+1][self.cur_x] == 0 and 
            main_list[self.cur_y+1][self.cur_x-1] == 0):

            main_list[self.cur_y][self.cur_x+1] = 1
            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y+1][self.cur_x] = 1
            main_list[self.cur_y+1][self.cur_x-1] = 1
            
            if (main_list[2][4] == 1 or main_list[2][5] == 1 or
                main_list[1][6] == 1):
                self.status = "UnableToPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[1,4,"add"],[1,5,"add"],
                                         [0,5,"add"],[0,6,"add"]]]
                
        
        
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        
        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []

        if (self.rotation == 0):
            if self.cur_y == 18:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+2][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+2][self.cur_x] == 1 or
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+2,self.cur_x-1,"add"],
                               [self.cur_y+2,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        elif (self.rotation == 1):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                if (main_list[self.cur_y+1][self.cur_x] == 1 or 
                    main_list[self.cur_y+2][self.cur_x+1] == 1):
                    self.status = "InPlace"
                    
                else:
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1, self.cur_x, "add"],
                               [self.cur_y+2, self.cur_x+1, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y, self.cur_x+1, "sub"]]
                    self.cur_y += 1
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        # Rotation = 0
        if (self.rotation == 0):
            # Move piece left
            if char == "1":
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-2] == 0):
                
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-2] = 1 
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-2,"add"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
            else:
                # Move piece right
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1 
                    
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x-1,"sub"]]
                    
                    self.cur_x += 1
            
            return [main_list, 0, updates]
        
        # Rotation = 1
        else:
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x+2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x+2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x+2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        updates = []
        
        if (self.rotation == 0):       
            if (self.cur_y == 0):
                return [main_list, 0, []]
            
            if (main_list[self.cur_y-1][self.cur_x] == 0 and
                main_list[self.cur_y+1][self.cur_x+1] == 0):
            
                main_list[self.cur_y-1][self.cur_x] = 1
                main_list[self.cur_y+1][self.cur_x+1] = 1
                
                main_list[self.cur_y+1][self.cur_x] = 0
                main_list[self.cur_y+1][self.cur_x-1] = 0
                
                updates = [[self.cur_y-1,self.cur_x,"add"],
                           [self.cur_y+1,self.cur_x+1,"add"],
                           [self.cur_y+1,self.cur_x,"sub"],
                           [self.cur_y+1,self.cur_x+-11,"sub"]]
                self.rotation = 1
        
        # Rotation = 1
        else:
            if (self.cur_x == 0):
                return [main_list, 0, []]
            
            if (main_list[self.cur_y+1][self.cur_x] == 0 and
                main_list[self.cur_y+1][self.cur_x-1] == 0):
            
                main_list[self.cur_y+1][self.cur_x] = 1
                main_list[self.cur_y+1][self.cur_x-1] = 1
                
                main_list[self.cur_y-1][self.cur_x] = 0
                main_list[self.cur_y+1][self.cur_x+1] = 0
                
                updates = [[self.cur_y+1,self.cur_x,"add"],
                           [self.cur_y+1,self.cur_x-1,"add"],
                           [self.cur_y-1,self.cur_x,"sub"],
                           [self.cur_y+1,self.cur_x+1,"sub"]]
                self.rotation = 0
            
        return [main_list, 0, updates]
    
    
    def get_y_interval(self):
        if self.rotation == 0:
            return [self.cur_y, self.cur_y+1]
        else:
            return [self.cur_y-1, self.cur_y, self.cur_y+1]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"










class SquarePiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 0
        self.cur_x = 4
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        """This function is called at the start of the game or when a piece has
        been placed.
        
        
        """
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x] == 0 and 
            main_list[self.cur_y][self.cur_x+1] == 0 and
            main_list[self.cur_y+1][self.cur_x] == 0 and 
            main_list[self.cur_y+1][self.cur_x+1] == 0):

            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y][self.cur_x+1] = 1
            main_list[self.cur_y+1][self.cur_x] = 1
            main_list[self.cur_y+1][self.cur_x+1] = 1
            
            if (main_list[2][4] == 1 or main_list[2][5] == 1):
                self.status = "UnableToPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[0,4,"add"],[0,5,"add"],
                                         [1,4,"add"],[1,5,"add"]]]
                
        
    
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        
        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []
     
        if self.cur_y == 18:
            self.status = "InPlace"
                
        else:
            if (main_list[self.cur_y+2][self.cur_x] == 1 or 
                main_list[self.cur_y+2][self.cur_x+1] == 1):
                self.status = "InPlace"
                
            else:
                main_list[self.cur_y+2][self.cur_x] = 1
                main_list[self.cur_y+2][self.cur_x+1] = 1
                
                main_list[self.cur_y][self.cur_x] = 0
                main_list[self.cur_y][self.cur_x+1] = 0
            
                updates = [[self.cur_y+2,self.cur_x,"add"],
                           [self.cur_y+2,self.cur_x+1,"add"],
                           [self.cur_y,self.cur_x,"sub"],
                           [self.cur_y,self.cur_x+1,"sub"]]
                self.cur_y += 1
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        
        # Move left
        if char == "1":
            if (self.cur_x == 0):
                    return [main_list, 0, []]
                
            elif (main_list[self.cur_y][self.cur_x-1] == 0 and
                main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                main_list[self.cur_y][self.cur_x-1] = 1
                main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                main_list[self.cur_y][self.cur_x+1] = 0
                main_list[self.cur_y+1][self.cur_x+1] = 0
                
                updates = [[self.cur_y,self.cur_x-1,"add"],
                           [self.cur_y+1,self.cur_x-1,"add"],
                           [self.cur_y,self.cur_x+1,"sub"],
                           [self.cur_y+1,self.cur_x+1,"sub"]]
                self.cur_x -= 1
        
        # Move right
        else:
            if (self.cur_x == 8):
                return [main_list, 0, []]
                
            elif (main_list[self.cur_y][self.cur_x+2] == 0 and
                  main_list[self.cur_y+1][self.cur_x+2] == 0):
                
                main_list[self.cur_y][self.cur_x+2] = 1
                main_list[self.cur_y+1][self.cur_x+2] = 1
                
                main_list[self.cur_y][self.cur_x] = 0
                main_list[self.cur_y+1][self.cur_x] = 0
                    
                updates = [[self.cur_y,self.cur_x+2,"add"],
                           [self.cur_y+1,self.cur_x+2,"add"],
                           [self.cur_y,self.cur_x,"sub"],
                           [self.cur_y+1,self.cur_x,"sub"]]
                self.cur_x += 1
            
        return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        
        return [main_list, 0, []]
    
    
    def get_y_interval(self):
        return [self.cur_y, self.cur_y+1]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 0
        self.cur_x = 4
        self.cur_y = 0
        self.status = "NotPlaced"










class TPiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x-1] == 0 and 
            main_list[self.cur_y][self.cur_x] == 0 and
            main_list[self.cur_y][self.cur_x+1] == 0 and 
            main_list[self.cur_y+1][self.cur_x] == 0):

            main_list[self.cur_y][self.cur_x-1] = 1
            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y][self.cur_x+1] = 1
            main_list[self.cur_y+1][self.cur_x] = 1
            
            if (main_list[1][4] == 1 or main_list[2][5] == 1 or
                main_list[1][6] == 1):
                self.status = "InPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[0,4,"add"],[0,5,"add"],
                                         [0,6,"add"],[1,5,"add"]]]
        
        
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        
        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []

        if (self.rotation == 0):
            if self.cur_y == 18:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+2][self.cur_x] == 1 or
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+2,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        elif (self.rotation == 1):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                
                if (main_list[self.cur_y+2][self.cur_x] == 1 or 
                    main_list[self.cur_y+1][self.cur_x-1] == 1):
                    self.status = "InPlace"
                else:
                
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y+1, self.cur_x-1, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y, self.cur_x-1, "sub"]]
                    self.cur_y += 1
                    
        elif (self.rotation == 2):
            if self.cur_y == 19:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+1][self.cur_x] == 1 or
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        # Rotation = 3
        else:
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                
                if (main_list[self.cur_y+2][self.cur_x] == 1 or 
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                    self.status = "InPlace"
                else:
                
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y+1, self.cur_x+1, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y, self.cur_x+1, "sub"]]
                    self.cur_y += 1
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        
        # Rotation = 0
        if (self.rotation == 0):
            # Move piece left
            if char == "1":
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x-2] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1 
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
            else:
                # Move piece right
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1 
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
            
            return [main_list, 0, updates]
        
        # Rotation = 1
        elif (self.rotation == 1):
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-2] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
        
        # Rotation = 2
        elif (self.rotation == 2):
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x-1] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
        
        # Rotation = 3
        elif (self.rotation == 3):
            # Rotation = 1
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        updates = []
        
        # Rotation anti-clockwise
        if (char == "z"):
            # Rotate from 0 to 3
            if (self.rotation == 0):
                if (self.cur_y == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x] == 0):
                
                    main_list[self.cur_y-1][self.cur_x] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    self.rotation = 3
                    
            # Rotate from 1 to 0
            elif (self.rotation == 1): 
                if (main_list[self.cur_y][self.cur_x+1] == 0):
                
                    main_list[self.cur_y][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"]]
                    self.rotation = 0
                    
            # Rotate from 2 to 1
            elif (self.rotation == 2):
                if (self.cur_y == 19):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+1][self.cur_x] == 0):
                
                    main_list[self.cur_y+1][self.cur_x] = 1
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.rotation = 1
                    
            # Rotate from 3 to 2
            elif (self.rotation == 3):
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x-1] == 0):
                
                    main_list[self.cur_y][self.cur_x-1] = 1
                    
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.rotation = 2
                    
        # Rotation clockwise
        else:
            # Rotate from 0 to 1
            if (self.rotation == 0):
                if (self.cur_y == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x] == 0):
                
                    main_list[self.cur_y-1][self.cur_x] = 1
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.rotation = 1
                    
            # Rotate from 1 to 2
            elif (self.rotation == 1):
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x+1] == 0):
                
                    main_list[self.cur_y][self.cur_x+1] = 1
                    
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.rotation = 2
                    
            # Rotate from 2 to 3
            elif (self.rotation == 2):
                if (self.cur_y == 19):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+1][self.cur_x] == 0):
                
                    main_list[self.cur_y+1][self.cur_x] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    self.rotation = 3
            
            # Rotate from 3 to 0
            else:
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x-1] == 0):
                
                    main_list[self.cur_y][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"]]
                    self.rotation = 0
            
                    
        return [main_list, 0, updates]
    
    
    def get_y_interval(self):
        if (self.rotation == 0):
            return [self.cur_y, self.cur_y+1]
        elif (self.rotation == 2):
            return [self.cur_y-1, self.cur_y]
        else:
            return [self.cur_y-1, self.cur_y, self.cur_y+1]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
        
        
        
        
        
        
        
        
class ReverseLPiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x-1] == 0 and 
            main_list[self.cur_y][self.cur_x] == 0 and
            main_list[self.cur_y][self.cur_x+1] == 0 and 
            main_list[self.cur_y+1][self.cur_x+1] == 0):

            main_list[self.cur_y][self.cur_x-1] = 1
            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y][self.cur_x+1] = 1
            main_list[self.cur_y+1][self.cur_x+1] = 1
            
            if (main_list[1][4] == 1 or main_list[1][5] == 1 or
                main_list[2][6] == 1):
                self.status = "UnableToPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[0,4,"add"],[0,5,"add"],
                                         [0,6,"add"],[1,6,"add"]]]
                
        
        
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        
        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []

        if (self.rotation == 0):
            if self.cur_y == 18:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+1][self.cur_x] == 1 or
                    main_list[self.cur_y+2][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+2,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        
        elif (self.rotation == 1):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                
                if (main_list[self.cur_y+2][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+2][self.cur_x] == 1):
                    self.status = "InPlace"
                else:
                
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y+2, self.cur_x-1, "add"],
                               [self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y+1, self.cur_x-1, "sub"]]
                    self.cur_y += 1
        
        
        if (self.rotation == 2):
            if self.cur_y == 19:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+1][self.cur_x] == 1 or
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y-1,self.cur_x-1,"sub"]]
                    self.cur_y += 1
        
        
        elif (self.rotation == 3):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                
                if (main_list[self.cur_y+2][self.cur_x] == 1 or 
                    main_list[self.cur_y][self.cur_x+1] == 1):
                    self.status = "InPlace"
                else:
                
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y, self.cur_x+1, "add"],
                               [self.cur_y-1, self.cur_x, "sub"],
                               [self.cur_y-1, self.cur_x+1, "sub"]]
                    self.cur_y += 1
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        # Rotation = 0
        if (self.rotation == 0):
            # Move piece left
            if char == "1":
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x-2] == 0 and
                    main_list[self.cur_y+1][self.cur_x] == 0):
                
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y+1][self.cur_x] = 1 
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
            else:
                # Move piece right
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x+2] == 0):
                
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x+2] = 1 
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x+2,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    
                    self.cur_x += 1
            
            return [main_list, 0, updates]
        
        # Rotation = 1
        elif (self.rotation == 1):
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x-1] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x-1,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
        
        # Rotation = 2
        elif (self.rotation == 2):
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-2] == 0 and
                    main_list[self.cur_y][self.cur_x-2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-2] = 1
                    main_list[self.cur_y][self.cur_x-2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-2,"add"],
                               [self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y-1,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x] == 0 and
                    main_list[self.cur_y][self.cur_x+2] == 0):
                
                    main_list[self.cur_y-1][self.cur_x] = 1
                    main_list[self.cur_y][self.cur_x+2] = 1
                    
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x-1] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y-1,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x-1,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
        
        # Rotation = 3
        elif (self.rotation == 3):
            # Rotation = 1
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+2] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+2] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x+2,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        updates = []
        
        # Rotation anti-clockwise
        if (char == "z"):
            # Rotate from 0 to 3
            if (self.rotation == 0):
                if (self.cur_y == 18):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+1][self.cur_x-1] == 0 and
                    main_list[self.cur_y+2][self.cur_x-1] == 0):
                
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+2,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_y += 1
                    self.cur_x -= 1
                    self.rotation = 3
                    
            # Rotate from 1 to 0
            elif (self.rotation == 1):
                if (self.cur_x == 9):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x-1] == 0 and
                    main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x-1] = 1
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y][self.cur_x+1] = 1

                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x-1,"sub"]]
                    self.cur_y -= 1
                    self.rotation = 0
                    
            # Rotate from 2 to 1
            elif (self.rotation == 2):
                if (self.cur_y == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                    main_list[self.cur_y-2][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+1] = 1
                    main_list[self.cur_y-2][self.cur_x+1] = 1

                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x+1,"add"],
                               [self.cur_y-2,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y-1,self.cur_x-1,"sub"]]
                    self.cur_y -= 1
                    self.cur_x += 1
                    self.rotation = 1
                    
            # Rotate from 3 to 2
            elif (self.rotation == 3):
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1

                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x,"sub"]]
                    self.cur_y += 1
                    self.rotation = 2
                    
        # Rotation clockwise
        else:
            # Rotate from 0 to 1
            if (self.rotation == 0):
                if (self.cur_y == 18):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y+1][self.cur_x] == 0 and
                    main_list[self.cur_y+2][self.cur_x] == 0 and
                    main_list[self.cur_y+2][self.cur_x-1] == 0):
                
                    main_list[self.cur_y+1][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x-1] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x,"add"],
                               [self.cur_y+2,self.cur_x,"add"],
                               [self.cur_y+2,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_y += 1
                    self.rotation = 1
                    
            # Rotate from 1 to 2
            elif (self.rotation == 1):
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y][self.cur_x-2] == 0 and
                    main_list[self.cur_y+1][self.cur_x-2] == 0):
                
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y+1][self.cur_x-2] = 1

                    main_list[self.cur_y-1][self.cur_x] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y+1,self.cur_x-2,"add"],
                               [self.cur_y-1,self.cur_x,"sub"],
                               [self.cur_y,self.cur_x,"sub"]]
                    self.cur_y += 1
                    self.cur_x -= 1
                    self.rotation = 2
                    
            # Rotate from 2 to 3
            elif (self.rotation == 2):
                if (self.cur_y == 1):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x] == 0 and
                    main_list[self.cur_y-2][self.cur_x] == 0 and
                    main_list[self.cur_y-2][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x] = 1
                    main_list[self.cur_y-2][self.cur_x] = 1
                    main_list[self.cur_y-2][self.cur_x+1] = 1

                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y-1][self.cur_x-1] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y-2,self.cur_x,"add"],
                               [self.cur_y-2,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y-1,self.cur_x-1,"sub"]]
                    self.cur_y -= 1
                    self.rotation = 3
            
            # Rotate from 3 to 0
            elif (self.rotation == 3):
                
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y-1][self.cur_x+2] == 0):
                
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y-1][self.cur_x+2] = 1
                    
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y-1,self.cur_x+2,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_y -= 1
                    self.cur_x += 1
                    self.rotation = 0
            
                    
        return [main_list, 0, updates]
    
    
    def get_y_interval(self):
        if self.rotation == 0:
            return [self.cur_y, self.cur_y+1]
        elif self.rotation == 2:
            return [self.cur_y-1, self.cur_y]
        else:
            return [self.cur_y-1, self.cur_y, self.cur_y+1]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
    
    
    
    
    
    
    
    
    
class SquigglyReverseLPiece():
    
    def __init__(self):
        """Initiate long piece.
  
        rotation = 0 means the pieces is placed vertically, 1 horizontally.
        
        The pieces have certain squares that are the central coordinates (cur_x 
        and cur_y). These are changed as the piece is moved or rotated.
        
        The status specifies the state of the game:
            NotPlaced: A piece is still falling.
            InPlace: A piece is either at the bottom or is blocked by another
                piece.
            UnableToPlace: The piece cannot be placed as there are squares
                in the way. The game is lost here.
        """
        
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"
        
        
    def init_placement(self, main_list):
        
        #print("Init: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))

        if (main_list[self.cur_y][self.cur_x] == 0 and 
            main_list[self.cur_y][self.cur_x-1] == 0 and
            main_list[self.cur_y+1][self.cur_x] == 0 and 
            main_list[self.cur_y+1][self.cur_x+1] == 0):

            main_list[self.cur_y][self.cur_x] = 1
            main_list[self.cur_y][self.cur_x-1] = 1
            main_list[self.cur_y+1][self.cur_x] = 1
            main_list[self.cur_y+1][self.cur_x+1] = 1
            
            if (main_list[1][4] == 1 or main_list[2][5] == 1 or
                main_list[2][6] == 1):
                self.status = "UnableToPlace"
            
        else:
            self.status = "UnableToPlace"
            
        return [main_list, self.status, [[0,4,"add"],[0,5,"add"],
                                         [1,5,"add"],[1,6,"add"]]]
                
        
        
    def check_drop_ability(self, main_list):
        """Check whether the piece can move down."""
        
        #print("Drop: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ", rotation = " + str(self.rotation))
        updates = []

        if (self.rotation == 0):
            if self.cur_y == 18:
                self.status = "InPlace"
                
            else:    
                if (main_list[self.cur_y+1][self.cur_x-1] == 1 or 
                    main_list[self.cur_y+2][self.cur_x] == 1 or
                    main_list[self.cur_y+2][self.cur_x+1] == 1):
                        self.status = "InPlace"
                else:
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+2][self.cur_x+1] = 1
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y+2,self.cur_x,"add"],
                               [self.cur_y+2,self.cur_x+1,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_y += 1
        
        elif (self.rotation == 1):
            if (self.cur_y == 18):
                self.status = "InPlace"
                
            else:
                if (main_list[self.cur_y+2][self.cur_x] == 1 or 
                    main_list[self.cur_y+1][self.cur_x+1] == 1):
                    self.status = "InPlace"
                    
                else:
                    main_list[self.cur_y+2][self.cur_x] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    
                    updates = [[self.cur_y+2, self.cur_x, "add"],
                               [self.cur_y+1, self.cur_x+1, "add"],
                               [self.cur_y-1, self.cur_x+1, "sub"],
                               [self.cur_y, self.cur_x, "sub"]]
                    self.cur_y += 1
        
        return [main_list, self.status, updates]
    
    
    def move(self, main_list, char):
        #print("Move: y = " + str(self.cur_y) + ", x = " + str(self.cur_x), ", rotation = " + str(self.rotation))
        updates = []
        # Rotation = 0
        if (self.rotation == 0):
            # Move piece left
            if char == "1":
                if (self.cur_x == 1):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x-2] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y][self.cur_x-2] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1 
                    
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x+1] = 0
                    
                    updates = [[self.cur_y,self.cur_x-2,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x+1,"sub"]]
                    self.cur_x -= 1
            else:
                # Move piece right
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                elif (main_list[self.cur_y][self.cur_x+1] == 0 and
                    main_list[self.cur_y+1][self.cur_x+2] == 0):
                
                    main_list[self.cur_y][self.cur_x+1] = 1
                    main_list[self.cur_y+1][self.cur_x+2] = 1 
                    
                    main_list[self.cur_y][self.cur_x-1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y,self.cur_x+1,"add"],
                               [self.cur_y+1,self.cur_x+2,"add"],
                               [self.cur_y,self.cur_x-1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    
                    self.cur_x += 1
            
            return [main_list, 0, updates]
        
        # Rotation = 1
        else:
            if char == "1":
                # Piece is at the left wall
                if (self.cur_x == 0):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x] == 0 and
                    main_list[self.cur_y][self.cur_x-1] == 0 and
                    main_list[self.cur_y+1][self.cur_x-1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x] = 1
                    main_list[self.cur_y][self.cur_x-1] = 1
                    main_list[self.cur_y+1][self.cur_x-1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x+1] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0
                    
                    updates = [[self.cur_y-1,self.cur_x,"add"],
                               [self.cur_y,self.cur_x-1,"add"],
                               [self.cur_y+1,self.cur_x-1,"add"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x+1,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x -= 1
                    
            # Move piece right
            else:
                if (self.cur_x == 8):
                    return [main_list, 0, []]
                
                if (main_list[self.cur_y-1][self.cur_x+2] == 0 and
                    main_list[self.cur_y][self.cur_x+2] == 0 and
                    main_list[self.cur_y+1][self.cur_x+1] == 0):
                
                    main_list[self.cur_y-1][self.cur_x+2] = 1
                    main_list[self.cur_y][self.cur_x+2] = 1
                    main_list[self.cur_y+1][self.cur_x+1] = 1
                    
                    main_list[self.cur_y-1][self.cur_x+1] = 0
                    main_list[self.cur_y][self.cur_x] = 0
                    main_list[self.cur_y+1][self.cur_x] = 0

                    
                    updates = [[self.cur_y-1,self.cur_x+2,"add"],
                               [self.cur_y,self.cur_x+2,"add"],
                               [self.cur_y+1,self.cur_x+1,"add"],
                               [self.cur_y-1,self.cur_x+1,"sub"],
                               [self.cur_y,self.cur_x,"sub"],
                               [self.cur_y+1,self.cur_x,"sub"]]
                    self.cur_x += 1
                    
            return [main_list, 0, updates]
    
    
    def rotate(self, main_list, char):
        #print("Rotation: y = " + str(self.cur_y) + ", x = " + str(self.cur_x) + ",rotation = " + str(self.rotation))
        updates = []
        
        if (self.rotation == 0):       
            if (self.cur_y == 0):
                return [main_list, 0, []]
            
            if (main_list[self.cur_y-1][self.cur_x+1] == 0 and
                main_list[self.cur_y][self.cur_x+1] == 0):
            
                main_list[self.cur_y-1][self.cur_x+1] = 1
                main_list[self.cur_y][self.cur_x+1] = 1
                
                main_list[self.cur_y][self.cur_x-1] = 0
                main_list[self.cur_y+1][self.cur_x+1] = 0
                
                updates = [[self.cur_y-1,self.cur_x+1,"add"],
                           [self.cur_y,self.cur_x+1,"add"],
                           [self.cur_y,self.cur_x-1,"sub"],
                           [self.cur_y+1,self.cur_x+1,"sub"]]
                self.rotation = 1
        
        # Rotation = 1
        else:
            if (self.cur_x == 0):
                return [main_list, 0, []]
            
            if (main_list[self.cur_y][self.cur_x-1] == 0 and
                main_list[self.cur_y+1][self.cur_x+1] == 0):
            
                main_list[self.cur_y][self.cur_x-1] = 1
                main_list[self.cur_y+1][self.cur_x+1] = 1
                
                main_list[self.cur_y-1][self.cur_x+1] = 0
                main_list[self.cur_y][self.cur_x+1] = 0
                
                updates = [[self.cur_y,self.cur_x-1,"add"],
                           [self.cur_y+1,self.cur_x+1,"add"],
                           [self.cur_y-1,self.cur_x+1,"sub"],
                           [self.cur_y,self.cur_x+1,"sub"]]
                self.rotation = 0
            
        return [main_list, 0, updates]
    
    
    def get_y_interval(self):
        if self.rotation == 0:
            return [self.cur_y, self.cur_y+1]
        else:
            return [self.cur_y-1, self.cur_y, self.cur_y+1]
    
        
    def reset(self):
        """Reset piece"""
        self.rotation = 0
        self.cur_x = 5
        self.cur_y = 0
        self.status = "NotPlaced"