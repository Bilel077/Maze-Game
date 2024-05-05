from collections import deque
import turtle

class Graphe:
    def __init__(self, L, C):
        self.L = L
        self.C = C
        self.graphe = {(0, 0): []}


    def ajouterNoeud(self, i, j):
        if (i, j) not in self.graphe.keys():
            self.graphe[(i, j)] = []

    def ajouterArc(self, c1, c2, porte=False):
        if c2 in self.graphe.keys() and c1 in self.graphe.keys() and ((c2),True) not in self.graphe[c1] and ((c2),False) not in self.graphe[c1] and ((c1),True) not in self.graphe[c2] and ((c1),False) not in self.graphe[c2] :
            self.graphe[c1].append((c2, porte))
            self.graphe[c2].append((c1, porte))

    def listerNoeuds(self):
        return self.graphe.keys()

    def listerArcs(self, c):
        if c not in self.graphe.keys():
            return self.graphe.values()

    def adjacenceNoeud(self, c1, c2):
        l = self.graphe[c1]
        return (c2, True) in l or (c2, False) in l

    def AfficherGraphe(self):
        print("Graphe:")
        for sommet, voisins in self.graphe.items():
            print(sommet, ": ", voisins)
    def successeur(self,k):
        l=[]
        for i in g.graphe[k]:
            if i[1]==True:
                l.append(i[0])
        return l
    
    
    
    def ajouterArcsVoisins(self):
        
        
        self.ajouterArc((0, 0), (0, 1),True)
        self.ajouterArc((0, 0), (1, 0),True)
        self.ajouterArc((0, 1), (1, 1),False)
        self.ajouterArc((0, 1), (0, 2),True)
        self.ajouterArc((0, 2), (1, 2),False)
        self.ajouterArc((0, 2), (0, 3),True)
        self.ajouterArc((0, 3), (0, 4),True)
        self.ajouterArc((0, 3), (1, 3),False)
        self.ajouterArc((0, 4), (0, 5),True)
        self.ajouterArc((0, 4), (1, 4),False)
        self.ajouterArc((0, 5), (0, 6),False)
        self.ajouterArc((0, 5), (1, 5),True)
        self.ajouterArc((0, 6), (0, 7),True)
        self.ajouterArc((0, 6), (1, 6),True)
        self.ajouterArc((0, 7), (0, 8),True)
        self.ajouterArc((0, 7), (1, 7),True)
        self.ajouterArc((0, 8), (0, 9),True)
        self.ajouterArc((0, 8), (1, 8),False)
        self.ajouterArc((0, 9), (0, 10),True)
        self.ajouterArc((0, 9), (1, 9),False)
        self.ajouterArc((0, 10), (0, 11),True)
        self.ajouterArc((0, 10), (1, 10),False)
        self.ajouterArc((0, 11), (0, 12),False)
        self.ajouterArc((0, 11), (1, 11),True)
        self.ajouterArc((0, 12), (0, 13),True)
        self.ajouterArc((0, 12), (1, 12),True)
        self.ajouterArc((0, 13), (0, 14),True)
        self.ajouterArc((0, 13), (1, 13),False)
        self.ajouterArc((0, 14), (1, 14),True)
        
        
        
        self.ajouterArc((1, 0), (1, 1),False)
        self.ajouterArc((1, 0), (2, 0),True)
        
        self.ajouterArc((1, 1), (1, 2),True)
        self.ajouterArc((1, 1), (2, 1),True)
        
        self.ajouterArc((1, 2), (1, 3),False)
        self.ajouterArc((1, 2), (2, 2),False)
        
        self.ajouterArc((1, 3), (1, 4),True)
        self.ajouterArc((1, 3), (2, 3),True)
        
        self.ajouterArc((1, 4), (1, 5),True)
        self.ajouterArc((1, 4), (2, 4),False)
        
        self.ajouterArc((1, 5), (1, 6),False)
        self.ajouterArc((1, 5), (2, 5),True)
        
        self.ajouterArc((1, 6), (1, 7),False)
        self.ajouterArc((1, 6), (2, 6),True)
        
        self.ajouterArc((1, 7), (1, 8),True)
        self.ajouterArc((1, 7), (2, 7),False)
        
        self.ajouterArc((1, 8), (1, 9),True)
        self.ajouterArc((1, 8), (2, 8),False)
        
        self.ajouterArc((1, 9), (1, 10),False)
        self.ajouterArc((1, 9), (2, 9),True)
        
        self.ajouterArc((1, 10), (1, 11),True)
        self.ajouterArc((1, 10), (2, 10),False)
        
        self.ajouterArc((1, 11), (1, 12),False)
        self.ajouterArc((1, 11), (2, 11),False)
        
        self.ajouterArc((1, 12), (1, 13),True)
        self.ajouterArc((1, 12), (2, 12),False)
        
        self.ajouterArc((1, 13), (1, 14),False)
        self.ajouterArc((1, 13), (2, 13),True)
        
        self.ajouterArc((1, 14), (2, 14),True)
        
        
        
        
        self.ajouterArc((2, 0), (2, 1),True)
        self.ajouterArc((2, 0), (3, 0),False)
        
        self.ajouterArc((2, 1), (2, 2),False)
        self.ajouterArc((2, 1), (3, 1),True)
        
        self.ajouterArc((2, 2), (2, 3),True)
        self.ajouterArc((2, 2), (3, 2),True)
        
        self.ajouterArc((2, 3), (2, 4),False)
        self.ajouterArc((2, 3), (3, 3),False)
        
        self.ajouterArc((2, 4), (2, 5),True)
        self.ajouterArc((2, 4), (3, 4),True)
        
        self.ajouterArc((2, 5), (2, 6),False)
        self.ajouterArc((2, 5), (3, 5),False)
        
        self.ajouterArc((2, 6), (2, 7),True)
        self.ajouterArc((2, 6), (3, 6),False)
        
        self.ajouterArc((2, 7), (2, 8),False)
        self.ajouterArc((2, 7), (3, 7),True)
        
        self.ajouterArc((2, 8), (2, 9),False)
        self.ajouterArc((2, 8), (3, 8),True)
        
        self.ajouterArc((2, 9), (2, 10),True)
        self.ajouterArc((2, 9), (3, 9),False)
        
        self.ajouterArc((2, 10), (2, 11),True)
        self.ajouterArc((2, 10), (3, 10),False)
        
        self.ajouterArc((2, 11), (2, 12),True)
        self.ajouterArc((2, 11), (3, 11),False)
        
        self.ajouterArc((2, 12), (2, 13),True)
        self.ajouterArc((2, 12), (3, 12),False)
        
        self.ajouterArc((2, 13), (2, 14),False)
        self.ajouterArc((2, 13), (3, 13),False)
        
        self.ajouterArc((2, 14), (3, 14),True)
        
        
        
        
        
        self.ajouterArc((3, 0), (3, 1),False)
        self.ajouterArc((3, 0), (4, 0),True)
        
        self.ajouterArc((3, 1), (3, 2),False)#
        self.ajouterArc((3, 1), (4, 1),True)
        
        self.ajouterArc((3, 2), (3, 3),False)
        self.ajouterArc((3, 2), (4, 2),True)#
        
        self.ajouterArc((3, 3), (3, 4),True)
        self.ajouterArc((3, 3), (4, 3),False)
        
        self.ajouterArc((3, 4), (3, 5),False)
        self.ajouterArc((3, 4), (4, 4),False)
        
        self.ajouterArc((3, 5), (3, 6),True)
        self.ajouterArc((3, 5), (4, 5),True)
        
        self.ajouterArc((3, 6), (3, 7),True)
        self.ajouterArc((3, 6), (4, 6),False)
        
        self.ajouterArc((3, 7), (3, 8),True)
        self.ajouterArc((3, 7), (4, 7),False)
        
        self.ajouterArc((3, 8), (3, 9),True)
        self.ajouterArc((3, 8), (4, 8),False)
        
        self.ajouterArc((3, 9), (3, 10),True)
        self.ajouterArc((3, 9), (4, 9),False)
        
        self.ajouterArc((3, 10), (3, 11),True)
        self.ajouterArc((3, 10), (4, 10),False)
        
        self.ajouterArc((3, 11), (3, 12),False)#
        self.ajouterArc((3, 11), (4, 11),False)
        
        self.ajouterArc((3, 12), (3, 13),True)
        self.ajouterArc((3, 12), (4, 12),True)#
        
        self.ajouterArc((3, 13), (3, 14),True)
        self.ajouterArc((3, 13), (4, 13),False)
        
        self.ajouterArc((3, 14), (4, 14),True)
        
        
        
        
        self.ajouterArc((4, 0), (4, 1),True)
        self.ajouterArc((4, 0), (5, 0),True)
        
        self.ajouterArc((4, 1), (4, 2),False)#
        self.ajouterArc((4, 1), (5, 1),False)
        
        self.ajouterArc((4, 2), (4, 3),False)
        self.ajouterArc((4, 2), (5, 2),True)#
        
        self.ajouterArc((4, 3), (4, 4),True)
        self.ajouterArc((4, 3), (5, 3),True)
        
        self.ajouterArc((4, 4), (4, 5),True)
        self.ajouterArc((4, 4), (5, 4),False)
        
        self.ajouterArc((4, 5), (4, 6),False)
        self.ajouterArc((4, 5), (5, 5),False)
        
        self.ajouterArc((4, 6), (4, 7),True)
        self.ajouterArc((4, 6), (5, 6),True)
        
        self.ajouterArc((4, 7), (4, 8),False)
        self.ajouterArc((4, 7), (5, 7),True)
        
        self.ajouterArc((4, 8), (4, 9),True)
        self.ajouterArc((4, 8), (5, 8),True)
        
        self.ajouterArc((4, 9), (4, 10),True)
        self.ajouterArc((4, 9), (5, 9),False)
        
        self.ajouterArc((4, 10), (4, 11),True)
        self.ajouterArc((4, 10), (5, 10),False)
        
        self.ajouterArc((4, 11), (4, 12),True)#
        self.ajouterArc((4, 11), (5, 11),False)
        
        self.ajouterArc((4, 12), (4, 13),False)
        self.ajouterArc((4, 12), (5, 12),False)#
        
        self.ajouterArc((4, 13), (4, 14),True)
        self.ajouterArc((4, 13), (5, 13),True)
        
        self.ajouterArc((4, 14), (5, 14),False)
        
        
        
        
        self.ajouterArc((5, 0), (5, 1),False)
        self.ajouterArc((5, 0), (6, 0),True)
        
        self.ajouterArc((5, 1), (5, 2),True)#
        self.ajouterArc((5, 1), (6, 1),True)
        
        self.ajouterArc((5, 2), (5, 3),False)
        self.ajouterArc((5, 2), (6, 2),False)#
        
        self.ajouterArc((5, 3), (5, 4),False)
        self.ajouterArc((5, 3), (6, 3),True)
        
        self.ajouterArc((5, 4), (5, 5),True)
        self.ajouterArc((5, 4), (6, 4),False)
        
        self.ajouterArc((5, 5), (5, 6),True)
        self.ajouterArc((5, 5), (6, 5),True)
        
        self.ajouterArc((5, 6), (5, 7),False)
        self.ajouterArc((5, 6), (6, 6),False)
        
        self.ajouterArc((5, 7), (5, 8),False)
        self.ajouterArc((5, 7), (6, 7),True)
        
        self.ajouterArc((5, 8), (5, 9),True)
        self.ajouterArc((5, 8), (6, 8),False)
        
        self.ajouterArc((5, 9), (5, 10),False)
        self.ajouterArc((5, 9), (6, 9),True)
        
        self.ajouterArc((5, 10), (5, 11),True)
        self.ajouterArc((5, 10), (6, 10),False)
        
        self.ajouterArc((5, 11), (5, 12),True)#
        self.ajouterArc((5, 11), (6, 11),True)
        
        self.ajouterArc((5, 12), (5, 13),False)
        self.ajouterArc((5, 12), (6, 12),True)#
        
        self.ajouterArc((5, 13), (5, 14),True)
        self.ajouterArc((5, 13), (6, 13),False)
        
        self.ajouterArc((5, 14), (6, 14),True)
        
        
        
        
        
        self.ajouterArc((6, 0), (6, 1),False)
        self.ajouterArc((6, 0), (7, 0),True)
        
        self.ajouterArc((6, 1), (6, 2),True)
        self.ajouterArc((6, 1), (7, 1),False)
        
        self.ajouterArc((6, 2), (6, 3),True)
        self.ajouterArc((6, 2), (7, 2),False)
        
        self.ajouterArc((6, 3), (6, 4),False)
        self.ajouterArc((6, 3), (7, 3),False)
        
        self.ajouterArc((6, 4), (6, 5),True)
        self.ajouterArc((6, 4), (7, 4),True)
        
        self.ajouterArc((6, 5), (6, 6),False)
        self.ajouterArc((6, 5), (7, 5),True)
        
        self.ajouterArc((6, 6), (6, 7),True)
        self.ajouterArc((6, 6), (7, 6),False)
        
        self.ajouterArc((6, 7), (6, 8),True)
        self.ajouterArc((6, 7), (7, 7),False)
        
        self.ajouterArc((6, 8), (6, 9),False)
        self.ajouterArc((6, 8), (7, 8),True)
        
        self.ajouterArc((6, 9), (6, 10),True)
        self.ajouterArc((6, 9), (7, 9),False)
        
        self.ajouterArc((6, 10), (6, 11),False)
        self.ajouterArc((6, 10), (7, 10),True)
        
        self.ajouterArc((6, 11), (6, 12),False)#
        self.ajouterArc((6, 11), (7, 11),True)
        
        self.ajouterArc((6, 12), (6, 13),False)
        self.ajouterArc((6, 12), (7, 12),False)#
        
        self.ajouterArc((6, 13), (6, 14),True)
        self.ajouterArc((6, 13), (7, 13),True)
        
        self.ajouterArc((6, 14), (7, 14),False)
        
        
        
        self.ajouterArc((7, 0), (7, 1),True)
        self.ajouterArc((7, 0), (8, 0),False)
        
        self.ajouterArc((7, 1), (7, 2),True)
        self.ajouterArc((7, 1), (8, 1),False)
        
        self.ajouterArc((7, 2), (7, 3),True)
        self.ajouterArc((7, 2), (8, 2),False)
        
        self.ajouterArc((7, 3), (7, 4),True)
        self.ajouterArc((7, 3), (8, 3),False)
        
        self.ajouterArc((7, 4), (7, 5),False)
        self.ajouterArc((7, 4), (8, 4),True)
        
        self.ajouterArc((7, 5), (7, 6),False)#
        self.ajouterArc((7, 5), (8, 5),False)
        
        self.ajouterArc((7, 6), (7, 7),True)
        self.ajouterArc((7, 6), (8, 6),True)#
        
        self.ajouterArc((7, 7), (7, 8),False)
        self.ajouterArc((7, 7), (8, 7),True)
        
        self.ajouterArc((7, 8), (7, 9),True)
        self.ajouterArc((7, 8), (8, 8),True)
        
        self.ajouterArc((7, 9), (7, 10),False)
        self.ajouterArc((7, 9), (8, 9),False)
        
        self.ajouterArc((7, 10), (7, 11),False)
        self.ajouterArc((7, 10), (8, 10),True)
        
        self.ajouterArc((7, 11), (7, 12),True)
        self.ajouterArc((7, 11), (8, 11),True)
        
        self.ajouterArc((7, 12), (7, 13),False)
        self.ajouterArc((7, 12), (8, 12),True)
        
        self.ajouterArc((7, 13), (7, 14),True)
        self.ajouterArc((7, 13), (8, 13),False)
        
        self.ajouterArc((7, 14), (8, 14),True)
        
        
        
        
        
        self.ajouterArc((8, 0), (8, 1),False)
        self.ajouterArc((8, 0), (9, 0),True)
        
        self.ajouterArc((8, 1), (8, 2),True)
        self.ajouterArc((8, 1), (9, 1),True)
        
        self.ajouterArc((8, 2), (8, 3),False)
        self.ajouterArc((8, 2), (9, 2),True)
        
        self.ajouterArc((8, 3), (8, 4),True)
        self.ajouterArc((8, 3), (9, 3),True)
        
        self.ajouterArc((8, 4), (8, 5),False)
        self.ajouterArc((8, 4), (9, 4),False)
        
        self.ajouterArc((8, 5), (8, 6),True)
        self.ajouterArc((8, 5), (9, 5),True)
        
        self.ajouterArc((8, 6), (8, 7),False)#
        self.ajouterArc((8, 6), (9, 6),False)
        
        self.ajouterArc((8, 7), (8, 8),False)
        self.ajouterArc((8, 7), (9, 7),True)#
        
        self.ajouterArc((8, 8), (8, 9),False)
        self.ajouterArc((8, 8), (9, 8),False)
        
        self.ajouterArc((8, 9), (8, 10),True)
        self.ajouterArc((8, 9), (9, 9),True)
        
        self.ajouterArc((8, 10), (8, 11),False)
        self.ajouterArc((8, 10), (9, 10),False)
        
        self.ajouterArc((8, 11), (8, 12),False)
        self.ajouterArc((8, 11), (9, 11),True)
        
        self.ajouterArc((8, 12), (8, 13),True)
        self.ajouterArc((8, 12), (9, 12),False)
        
        self.ajouterArc((8, 13), (8, 14),True)
        self.ajouterArc((8, 13), (9, 13),False)
        
        self.ajouterArc((8, 14), (9, 14),False)
        
        
        self.ajouterArc((9, 0), (9, 1),True)
        self.ajouterArc((9, 1), (9, 2),False)
        self.ajouterArc((9, 2), (9, 3),True)
        self.ajouterArc((9, 3), (9, 4),True)
        self.ajouterArc((9, 4), (9, 5),True)
        self.ajouterArc((9, 5), (9, 6),False)
        self.ajouterArc((9, 6), (9, 7),True)
        self.ajouterArc((9, 7), (9, 8),True)
        self.ajouterArc((9, 8), (9, 9),True)
        self.ajouterArc((9, 9), (9, 10),False)
        self.ajouterArc((9, 10), (9, 11),True)
        self.ajouterArc((9, 11), (9, 12),True)
        self.ajouterArc((9, 12), (9, 13),True)
        self.ajouterArc((9, 13), (9, 14),True)
        
        
                    
            #########################################    
    def AfficherLabyrinthe(self):
        turtle.speed(0)
        taille_case = 30
        path_founded=[(0,0)]
        for i in g.BFS((0,0),(9,14)):
            path_founded.append(i)
        
        color="#64FF00"
        start_color = "#FFD700"
        finish_color = "#00FFB6"

        for i in range(self.L):  
            for j in range(self.C): 
                x = j * taille_case
                y = -i * taille_case
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                if (i,j) in path_founded:
                    if (i, j) == (0, 0):
                        turtle.fillcolor(start_color)    
                    elif (i, j) == (9, 13):
                        turtle.fillcolor(finish_color)
                    else:
                        turtle.fillcolor(color)
                    turtle.begin_fill()
                if(not has_box_above(self.C,i,j)):
                    turtle.setheading(0)
                    turtle.forward(taille_case)
                else:
                    if ((i-1, j), False) in self.graphe.get((i, j), []):
                        turtle.setheading(0)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(0)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                
                if(not has_box_right(self.C,i,j)):
                    turtle.setheading(-90)
                    turtle.forward(taille_case)
                else:
                    if ((i, j+1), False) in self.graphe.get((i, j), []):
                        turtle.setheading(-90)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(-90)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                
                if(not has_box_below(self.C,i,j)):
                    turtle.setheading(180)
                    turtle.forward(taille_case)
                else:
                    if ((i+1, j), False) in self.graphe.get((i, j), []):
                        turtle.setheading(180)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(180)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                
                if(not has_box_left(self.C,i,j)):
                    turtle.setheading(90)
                    turtle.forward(taille_case)
                else:
                    if ((i, j-1), False) in self.graphe.get((i, j), []):
                        turtle.setheading(90)
                        turtle.forward(taille_case)
                    else:
                        turtle.setheading(90)
                        turtle.penup()
                        turtle.forward(taille_case)
                        turtle.pendown()
                # if (i, j) == (0, 0) or (i, j) == (9, 14):
                #     turtle.fillcolor("black")
                #     turtle.begin_fill()
                #     turtle.circle(5)  #black point 
                #     turtle.end_fill()        
                if (i,j) in path_founded:
                    turtle.end_fill()
        turtle.penup()
        turtle.goto(0, -self.L * taille_case)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(self.C * taille_case)
        turtle.hideturtle()
        turtle.done()
    # def laby(self,start,goal):
    #         for i in range(l):
    #             for j in range(c):
    #                 self.ajouterNoeud(i, j)            
    #         self.ajouterArcsVoisins()

            
    def BFS(self,start,goal):
        for i in range(l):
                for j in range(c):
                    self.ajouterNoeud(i, j)            
        self.ajouterArcsVoisins()
        
        pile=deque()
        pile.append(start)
        visited=[start]
        accessible={}
        while(len(pile)>0):
            x=pile.popleft()
            for voisin in self.successeur(x):
                if voisin not in visited:
                    accessible[voisin]=x
                    pile.append(voisin)
                    visited.append(voisin)
                    
        fwdPath={}
        cell=goal
        while cell!=(0,0):
            
                fwdPath[accessible[cell]]=cell
                cell=accessible[cell]
        print("Visited= ",len(visited))     
        return fwdPath
    
    # def DFS(self,start,goal):
    #     for i in range(l):
    #         for j in range(c):
    #             self.ajouterNoeud(i, j)            
    #     self.ajouterArcsVoisins()
        
    #     pile=deque()
    #     pile.append(start)
    #     visited=[start]
    #     accessible={}
    #     while(len(pile)>0):
    #         x=pile.pop()
    #         for voisin in self.successeur(x):
    #             if voisin not in visited:
    #                 accessible[voisin]=x
    #                 pile.append(voisin)
    #                 visited.append(voisin)
                    
    #     fwdPath={}
    #     cell=goal
    #     while cell!=(0,0):
            
    #             fwdPath[accessible[cell]]=cell
    #             cell=accessible[cell]
    #     print(len(visited))    
    #     return fwdPath
    # 


def has_box_above(l, row, col):
    if row == 0:  
        return False
    else:
        return True
def has_box_below(l, row, col):
    if row == l - 1: 
        return False
    else:
        return True
def has_box_left(l, row, col):
    if col == 0: 
        return False
    else:
        return True

def has_box_right(l, row, col):
    if col == l - 1:  
        return False
    else:
        return True

l=10
c=15
g = Graphe(l, c)
g.BFS((0,0),(9,14))
g.AfficherLabyrinthe()