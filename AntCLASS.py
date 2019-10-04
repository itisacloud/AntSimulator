import numpy as np
import random as rdm

class Food:
    def __init__(self,position):
        self.position = position
    def check_for_food

class Field:
    def __init__(self,board_size):
        self.board = np.zeros(board_size[0]*board_size[1],dtype=npbool).reshape(board_size)





class Ant:
    def __init__(self, start_position,board_size):
        self.position = array(start_position)
        self.lifetime = 80
        self.board_size = board_size
        self.max_distance = (self.board_size[0]**2+self.board_size[1]**2)//2
        self.critical_distance = 5
        self.path = []
        self.status = False

    def move(self, ants, field,  food):
        vector = array([0,0])

        if self.status:
            move = self.path[-1]




        if self.status == False:

            for ant in ants:

                connection = array(self.position)-array(ant.position)
                distance = ((connection[0]**2+connection[1]**2)//2)

                if distance < self.critical_distance:
                    weight = (1-(distance/self.critical_distance)**2)**2
                else:
                    weight = 0
                vector += connection*weight

            connection = array(self.position) - array(food.position)
            distance = ((connection[0] ** 2 + connection[1] ** 2) // 2)
            distance = np.hyplot(connection[0],connection[1])
            weight = 1 - distance/self.max_distance
            vector = connection*weight

            angle = np.arccos(vector[1]/(np.hyplot(vector[0],vector[1])))

            move = array([0,0])

            if angle >= 22.5 and angle < 157.5:
                self.move[1] += 1
            if angle >= 202.5 and angle < 337.5:
                self.move[1] -= 1]
            if angle < 67.5 or angle >= 292.5:
                self.move[0] += 1
            if angle > 112.5 or angle <= 247.5:
                self.move[0] -= 1

            for ant in ants:
                if (self.position + move) == ant.position:
                    return
            self.path.append(move)

        self.position += move

    def age(self):
        self.lifetime -= 1















