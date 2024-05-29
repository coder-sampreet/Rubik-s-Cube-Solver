class RubiksCube:
    def __init__(self):
        # Initialize the Rubik's Cube with the solved state
        self.cube = {
            'green': [['G1', 'G2', 'G3'],
                      ['G4', 'G5', 'G6'],
                      ['G7', 'G8', 'G9']],  # front
            'blue': [['B1', 'B2', 'B3'],
                     ['B4', 'B5', 'B6'],
                     ['B7', 'B8', 'B9']],   # back
            'white': [['W1', 'W2', 'W3'],
                      ['W4', 'W5', 'W6'],
                      ['W7', 'W8', 'W9']],  # top
            'yellow': [['Y1', 'Y2', 'Y3'],
                       ['Y4', 'Y5', 'Y6'],
                       ['Y7', 'Y8', 'Y9']], # bottom
            'orange': [['O1', 'O2', 'O3'],
                       ['O4', 'O5', 'O6'], 
                       ['O7', 'O8', 'O9']], # left
            'red': [['R1', 'R2', 'R3'],
                    ['R4', 'R5', 'R6'],
                    ['R7', 'R8', 'R9']]    # right
        }

    def input_cube_state(self):
        faces = ['green', 'blue', 'white', 'yellow', 'orange', 'red']
        for face in faces:
            print(f"Enter the pieces for the {face} face in row-major order (9 pieces, separated by spaces):")
            while True:
                pieces = input().split()
                if len(pieces) == 9:
                    self.cube[face] = [pieces[:3], pieces[3:6], pieces[6:]]
                    break
                else:
                    print("Invalid input. Please enter exactly 9 pieces.")

    def rotate_face_clockwise(self, face):
        # Rotate the stickers of a face clockwise
        
        old_face = self.cube[face]
        new_face = [
            [old_face[2][0], old_face[1][0], old_face[0][0]],
            [old_face[2][1], old_face[1][1], old_face[0][1]],
            [old_face[2][2], old_face[1][2], old_face[0][2]]
        ]
        self.cube[face] = new_face

        # Step 2: Rotate the adjacent edges
        if face == 'green':
            temp = self.cube['white'][2]
            self.cube['white'][2] = [self.cube['orange'][2][2], self.cube['orange'][1][2], self.cube['orange'][0][2]]
            self.cube['orange'][0][2], self.cube['orange'][1][2], self.cube['orange'][2][2] = self.cube['yellow'][0]
            self.cube['yellow'][0] = [self.cube['red'][2][0], self.cube['red'][1][0], self.cube['red'][0][0]]
            self.cube['red'][0][0], self.cube['red'][1][0], self.cube['red'][2][0] = temp

        elif face == 'blue':
            temp = self.cube['yellow'][2]
            self.cube['yellow'][2] = [self.cube['orange'][0][0], self.cube['orange'][1][0], self.cube['orange'][2][0]]
            self.cube['orange'][2][0], self.cube['orange'][1][0], self.cube['orange'][0][0] = self.cube['white'][0]
            self.cube['white'][0] = [self.cube['red'][0][2], self.cube['red'][1][2], self.cube['red'][2][2]]
            self.cube['red'][0][2], self.cube['red'][1][2], self.cube['red'][2][2] = temp[::-1]


        elif face == 'white':
            temp = self.cube['blue'][2]
            self.cube['blue'][2] = self.cube['orange'][0][::-1]
            self.cube['orange'][0] = self.cube['green'][0]
            self.cube['green'][0] = self.cube['red'][0]
            self.cube['red'][0] = temp[::-1]

        elif face == 'yellow':
            temp = self.cube['green'][2]
            self.cube['green'][2] = self.cube['orange'][2]
            self.cube['orange'][2] = self.cube['blue'][0][::-1]
            self.cube['blue'][0] = self.cube['red'][2][::-1]
            self.cube['red'][2] = temp

        elif face == 'orange':
            temp = [self.cube['white'][0][0],self.cube['white'][1][0],self.cube['white'][2][0]]
            self.cube['white'][0][0],self.cube['white'][1][0],self.cube['white'][2][0] = [self.cube['blue'][0][0],self.cube['blue'][1][0],self.cube['blue'][2][0]]
            self.cube['blue'][0][0],self.cube['blue'][1][0],self.cube['blue'][2][0] = [self.cube['yellow'][0][0],self.cube['yellow'][1][0],self.cube['yellow'][2][0]]
            self.cube['yellow'][0][0],self.cube['yellow'][1][0],self.cube['yellow'][2][0] =[self.cube['green'][0][0],self.cube['green'][1][0],self.cube['green'][2][0]]
            self.cube['green'][0][0],self.cube['green'][1][0],self.cube['green'][2][0] = temp

        elif face == 'red':
            temp = [self.cube['white'][2][2],self.cube['white'][1][2],self.cube['white'][0][2]]
            self.cube['white'][2][2],self.cube['white'][1][2],self.cube['white'][0][2] = [self.cube['green'][2][2],self.cube['green'][1][2],self.cube['green'][0][2]]
            self.cube['green'][2][2],self.cube['green'][1][2],self.cube['green'][0][2] = [self.cube['yellow'][2][2],self.cube['yellow'][1][2],self.cube['yellow'][0][2]]
            self.cube['yellow'][2][2],self.cube['yellow'][1][2],self.cube['yellow'][0][2] = [self.cube['blue'][2][2],self.cube['blue'][1][2],self.cube['blue'][0][2]]
            self.cube['blue'][2][2],self.cube['blue'][1][2],self.cube['blue'][0][2] = temp

    def rotate_face_counter_clockwise(self, face):
        # Rotate the stickers of a face counter-clockwise
        old_face = self.cube[face]
        new_face = [
            [old_face[0][2], old_face[1][2], old_face[2][2]],
            [old_face[0][1], old_face[1][1], old_face[2][1]],
            [old_face[0][0], old_face[1][0], old_face[2][0]]
        ]
        self.cube[face] = new_face

        # Step 2: Rotate the adjacent edges
        if face == 'green':
            temp = self.cube['white'][2]
            self.cube['white'][2] = [self.cube['red'][0][0], self.cube['red'][1][0], self.cube['red'][2][0]]
            self.cube['red'][0][0], self.cube['red'][1][0], self.cube['red'][2][0] = self.cube['yellow'][0][::-1]
            self.cube['yellow'][0] = [self.cube['orange'][0][2], self.cube['orange'][1][2], self.cube['orange'][2][2]]
            self.cube['orange'][0][2], self.cube['orange'][1][2], self.cube['orange'][2][2] = temp[::-1]

        elif face == 'blue':
            temp = self.cube['yellow'][2]
            self.cube['yellow'][2] = [self.cube['red'][2][2], self.cube['red'][1][2], self.cube['red'][0][2]]
            self.cube['red'][2][2], self.cube['red'][1][2], self.cube['red'][0][2] = self.cube['white'][0][::-1]
            self.cube['white'][0] = [self.cube['orange'][2][0], self.cube['orange'][1][0], self.cube['orange'][0][0]]
            self.cube['orange'][2][0], self.cube['orange'][1][0], self.cube['orange'][0][0] = temp[::-1]

        elif face == 'white':
            temp = self.cube['blue'][2]
            self.cube['blue'][2] = self.cube['red'][0][::-1]
            self.cube['red'][0] = self.cube['green'][0]
            self.cube['green'][0] = self.cube['orange'][0]
            self.cube['orange'][0] =temp[::-1]

        elif face == 'yellow':
            temp = self.cube['green'][2]
            self.cube['green'][2] = self.cube['red'][2]
            self.cube['red'][2] = self.cube['blue'][0][::-1]
            self.cube['blue'][0] = self.cube['orange'][2][::-1]
            self.cube['orange'][2] = temp

        elif face == 'orange':
            temp = [self.cube['white'][0][0],self.cube['white'][1][0],self.cube['white'][2][0]]
            self.cube['white'][0][0],self.cube['white'][1][0],self.cube['white'][2][0] = [self.cube['green'][0][0],self.cube['green'][1][0],self.cube['green'][2][0]]
            self.cube['green'][0][0],self.cube['green'][1][0],self.cube['green'][2][0] = [self.cube['yellow'][0][0],self.cube['yellow'][1][0],self.cube['yellow'][2][0]]
            self.cube['yellow'][0][0],self.cube['yellow'][1][0],self.cube['yellow'][2][0] = [self.cube['blue'][0][0],self.cube['blue'][1][0],self.cube['blue'][2][0]]
            self.cube['blue'][0][0],self.cube['blue'][1][0],self.cube['blue'][2][0] = temp

        elif face == 'red':
            temp = [self.cube['white'][2][2],self.cube['white'][1][2],self.cube['white'][0][2]]
            self.cube['white'][2][2],self.cube['white'][1][2],self.cube['white'][0][2] = [self.cube['blue'][2][2],self.cube['blue'][1][2],self.cube['blue'][0][2]]
            self.cube['blue'][2][2],self.cube['blue'][1][2],self.cube['blue'][0][2] = [self.cube['yellow'][2][2],self.cube['yellow'][1][2],self.cube['yellow'][0][2]]
            self.cube['yellow'][2][2],self.cube['yellow'][1][2],self.cube['yellow'][0][2] = [self.cube['green'][2][2],self.cube['green'][1][2],self.cube['green'][0][2]]
            self.cube['green'][2][2],self.cube['green'][1][2],self.cube['green'][0][2] = temp

    def check_face(self,color):
            if color == "R":
                return "red"
            elif color == "G":
                return "green"
            elif color == "B":
                return "blue"
            elif color == "Y":
                return "yellow"
            elif color == "O":
                return "orange"
            elif color == "W": 
                return "white"
    
    def perform_moves(self, moves):
        print(moves)
        for move in moves.split():
            if move.endswith("'"):
                self.rotate_face_counter_clockwise(self.check_face(move[0]))
            else:
                self.rotate_face_clockwise(self.check_face(move))

    def white_cross(self):
# if already crossed then skip
        if 'W' in self.cube['white'][2][1] and 'G' in self.cube['green'][0][1]:
            pass
        if 'W' in self.cube['white'][1][0] and 'O' in self.cube['orange'][0][1]:
            pass
        if 'W' in self.cube['white'][1][2] and 'R' in self.cube['red'][0][1]:
            pass
        if 'W' in self.cube['white'][0][1] and 'B' in self.cube['blue'][2][1]:
            pass

 # Logic for positioning each white edge piece

        # White-Green edge cases
        if 'G' in self.cube['white'][2][1] and 'W' in self.cube['green'][0][1]:  # right place but flipped c
            self.perform_moves("G G Y R G' R'")
        
        if 'W' in self.cube['white'][1][2] and 'G' in self.cube['red'][0][1]:  # on white-red edge c
            self.perform_moves("R' R' Y' G G")
        
        if 'G' in self.cube['white'][1][2] and 'W' in self.cube['red'][0][1]:  # on white-red edge but flipped c
            self.perform_moves("R' G'")
        
        if 'W' in self.cube['white'][1][0] and 'G' in self.cube['orange'][0][1]:  # on white-orange edge c
            self.perform_moves("O O Y G G")
        
        if 'G' in self.cube['white'][1][0] and 'W' in self.cube['orange'][0][1]:  # on white-orange edge but flipped c
            self.perform_moves("O G")
        
        if 'W' in self.cube['white'][0][1] and 'G' in self.cube['blue'][2][1]:  # on white-blue edge c
            self.perform_moves("B B Y Y G G")
        
        if 'G' in self.cube['white'][0][1] and 'W' in self.cube['blue'][2][1]:  # on white-blue edge but flipped c
            self.perform_moves("B B Y' R G' R'")
        
        if 'G' in self.cube['green'][1][2] and 'W' in self.cube['red'][1][0]:  # on green-red edge c
            self.perform_moves("G'")
        
        if 'W' in self.cube['green'][1][2] and 'G' in self.cube['red'][1][0]:  # on green-red edge but flipped c
            self.perform_moves("R' Y' R G G")
        
        if 'G' in self.cube['green'][1][0] and 'W' in self.cube['orange'][1][2]:  # on green-orange edge c
            self.perform_moves("G")
        
        if 'W' in self.cube['green'][1][0] and 'G' in self.cube['orange'][1][2]:  # on green-orange edge but flipped c
            self.perform_moves("O Y O' G G")
        
        if 'G' in self.cube['green'][2][1] and 'W' in self.cube['yellow'][0][1]:  # on green-yellow edge c
            self.perform_moves("G G")
        
        if 'W' in self.cube['green'][2][1] and 'G' in self.cube['yellow'][0][1]:  # on green-yellow edge but flipped c
            self.perform_moves("Y R G' R'")
        
        if 'G' in self.cube['red'][2][1] and 'W' in self.cube['yellow'][1][2]:  # on red-yellow edge c
            self.perform_moves("Y' G G")
        
        if 'W' in self.cube['red'][2][1] and 'G' in self.cube['yellow'][1][2]:  # on red-yellow edge but flipped c
            self.perform_moves("R G' R'")
        
        if 'G' in self.cube['orange'][2][1] and 'W' in self.cube['yellow'][1][0]:  # on orange-yellow edge c
            self.perform_moves("Y G G")
        
        if 'W' in self.cube['orange'][2][1] and 'G' in self.cube['yellow'][1][0]:  # on orange-yellow edge but flipped c
            self.perform_moves("O' G O")
        
        if 'G' in self.cube['blue'][0][1] and 'W' in self.cube['yellow'][2][1]:  # on blue-yellow edge c
            self.perform_moves("Y Y G G")
        
        if 'W' in self.cube['blue'][0][1] and 'G' in self.cube['yellow'][2][1]:  # on blue-yellow edge but flipped c
            self.perform_moves("Y' R G' R'")
        
        if 'G' in self.cube['red'][1][2] and 'W' in self.cube['blue'][1][2]:  # on red-blue edge c
            self.perform_moves("R Y' R' G G")
        
        if 'W' in self.cube['red'][1][2] and 'G' in self.cube['blue'][1][2]:  # on red-blue edge but flipped c
            self.perform_moves("R R G' R R")
        
        if 'G' in self.cube['orange'][1][0] and 'W' in self.cube['blue'][1][0]:  # on orange-blue edge c
            self.perform_moves("O' Y O G G")
        
        if 'W' in self.cube['orange'][1][0] and 'G' in self.cube['blue'][1][0]:  # on orange-blue edge but flipped c
            self.perform_moves("O O G O O")
        
        # White-Red edge cases
        if 'R' in self.cube['white'][1][2] and 'W' in self.cube['red'][0][1]:  # right place but flipped c
            self.perform_moves("R R Y' G' R G")
        
        if 'W' in self.cube['white'][0][1] and 'R' in self.cube['blue'][2][1]:  # on white-blue edge c
            self.perform_moves("B B Y' R R")
        
        if 'R' in self.cube['white'][0][1] and 'W' in self.cube['blue'][2][1]:  # on white-blue edge but flipped c
            self.perform_moves("B' R'")
        
        if 'W' in self.cube['white'][1][0] and 'R' in self.cube['orange'][0][1]:  # on white-orange edge c
            self.perform_moves("O O Y Y R R")
        
        if 'R' in self.cube['white'][1][0] and 'W' in self.cube['orange'][0][1]:  # on white-orange edge but flipped c
            self.perform_moves("O O Y G' R G")
        
        if 'W' in self.cube['white'][2][1] and 'R' in self.cube['green'][0][1]:  # on white-green edge c
            self.perform_moves("G G Y R R")
        
        if 'R' in self.cube['white'][2][1] and 'W' in self.cube['green'][0][1]:  # on white-green edge but flipped c
            self.perform_moves("G R")
        
        if 'R' in self.cube['red'][1][2] and 'W' in self.cube['blue'][1][2]:  # on red-blue edge c
            self.perform_moves("R'")
        
        if 'W' in self.cube['red'][1][2] and 'R' in self.cube['blue'][1][2]:  # on red-blue edge but flipped c
            self.perform_moves("B' Y' R R B")
        
        if 'R' in self.cube['red'][2][1] and 'W' in self.cube['yellow'][1][2]:  # on red-yellow edge c
            self.perform_moves("R R")
        
        if 'W' in self.cube['red'][2][1] and 'R' in self.cube['yellow'][1][2]:  # on red-yellow edge but flipped C
            self.perform_moves("Y' G' R G")
        
        if 'W' in self.cube['green'][1][2] and 'R' in self.cube['red'][1][0]:  # on green-red edge c
            self.perform_moves("R")
        
        if 'R' in self.cube['green'][1][2] and 'W' in self.cube['red'][1][0]:  # on green-red edge but flipped c
            self.perform_moves("R' Y' G' R G")
        
        if 'R' in self.cube['blue'][0][1] and 'W' in self.cube['yellow'][2][1]:  # on blue-yellow edge c
            self.perform_moves("Y' R R")
        
        if 'W' in self.cube['blue'][0][1] and 'R' in self.cube['yellow'][2][1]:  # on blue-yellow edge but flipped c
            self.perform_moves("B R' B'")
        
        if 'R' in self.cube['orange'][1][0] and 'W' in self.cube['blue'][1][0]:  # on orange-blue edge c
            self.perform_moves("O' Y Y O R R")
        
        if 'W' in self.cube['orange'][1][0] and 'R' in self.cube['blue'][1][0]:  # on orange-blue edge but flipped C
            self.perform_moves("O' Y G' R G O")

        if 'R' in self.cube['orange'][1][2] and 'W' in self.cube['green'][1][0]:  # on orange-green edge c
            self.perform_moves("O Y Y R R O'")

        if 'W' in self.cube['orange'][1][2] and 'R' in self.cube['green'][1][0]:  # on orange-green edge but flipped c
            self.perform_moves("G' Y R R G")

        if 'R' in self.cube['green'][2][1] and 'W' in self.cube['yellow'][0][1]:  # on green-yellow edge c
            self.perform_moves("Y R R")

        if 'W' in self.cube['green'][2][1] and 'R' in self.cube['yellow'][0][1]:  # on green-yellow edge but flipped c
            self.perform_moves("G' R G")

        if 'R' in self.cube['orange'][2][1] and 'W' in self.cube['yellow'][1][0]:  # on orange-yellow edge c
            self.perform_moves("Y Y R R")

        if 'W' in self.cube['orange'][2][1] and 'R' in self.cube['yellow'][1][0]:  # on orange-yellow edge BUT FLIPPEND c
            self.perform_moves("Y G' R G")
        
        # White-Blue edge cases
        if 'B' in self.cube['white'][0][1] and 'W' in self.cube['blue'][2][1]:  # right place but flipped C
            self.perform_moves("B B Y' R' B R")
        
        if 'W' in self.cube['white'][1][0] and 'B' in self.cube['orange'][0][1]:  # on white-orange edge C
            self.perform_moves("O O Y' B B")
        
        if 'B' in self.cube['white'][1][0] and 'W' in self.cube['orange'][0][1]:  # on white-orange edge but flipped C
            self.perform_moves("O' B'")
        
        if 'W' in self.cube['white'][1][2] and 'B' in self.cube['red'][0][1]:  # on white-red edge C
            self.perform_moves("R R Y B B")
        
        if 'B' in self.cube['white'][1][2] and 'W' in self.cube['red'][0][1]:  # on white-red edge but flipped C
            self.perform_moves("R B")
        
        if 'W' in self.cube['white'][2][1] and 'B' in self.cube['green'][0][1]:  # on white-green edge C
            self.perform_moves("G G Y Y B B")
        
        if 'B' in self.cube['white'][2][1] and 'W' in self.cube['green'][0][1]:  # on white-green edge but flipped C
            self.perform_moves("G G Y R' B R")
        
        if 'B' in self.cube['blue'][1][2] and 'W' in self.cube['red'][1][2]:  # on blue-red edge C
            self.perform_moves("B")
        
        if 'W' in self.cube['blue'][1][2] and 'B' in self.cube['red'][1][2]:  # on blue-red edge but flipped C
            self.perform_moves("R Y B B R'")
        
        if 'B' in self.cube['blue'][0][1] and 'W' in self.cube['yellow'][2][1]:  # on blue-yellow edge C
            self.perform_moves("B2")
        
        if 'W' in self.cube['blue'][0][1] and 'B' in self.cube['yellow'][2][1]:  # on blue-yellow edge but flipped C
            self.perform_moves("Y' R' B R")
        
        if 'W' in self.cube['orange'][1][0] and 'B' in self.cube['blue'][1][0]:  # on orange-blue edge C
            self.perform_moves("B'")
        
        if 'B' in self.cube['orange'][1][0] and 'W' in self.cube['blue'][1][0]:  # on orange-blue edge but flipped C
            self.perform_moves("O' Y' B B O")
        
        if 'B' in self.cube['green'][1][2] and 'W' in self.cube['red'][1][0]:  # on green-red edge C
            self.perform_moves("R R G R R")
        
        if 'W' in self.cube['green'][1][2] and 'B' in self.cube['red'][1][0]:  # on green-red edge but flipped C
            self.perform_moves("R Y R' B B")
        
        if 'B' in self.cube['red'][2][1] and 'W' in self.cube['yellow'][1][2]:  # on red-yellow edge C
            self.perform_moves("Y B B")
        
        if 'W' in self.cube['red'][2][1] and 'B' in self.cube['yellow'][1][2]:  # on red-yellow edge but flipped C
            self.perform_moves("R' B R")

        if 'W' in self.cube['orange'][1][2] and 'B' in self.cube['green'][1][0]:  # on orange-green edge c
            self.perform_moves("O O B' O O")

        if 'B' in self.cube['orange'][1][2] and 'W' in self.cube['green'][1][0]:  # on orange-green edge but flipped c
            self.perform_moves("O Y' B B O'")

        if 'B' in self.cube['green'][2][1] and 'W' in self.cube['yellow'][0][1]:  # on green-yellow edge c
            self.perform_moves("Y Y B B")

        if 'W' in self.cube['green'][2][1] and 'B' in self.cube['yellow'][0][1]:  # on green-yellow edge but flipped c
            self.perform_moves("Y R' B R")

        if 'B' in self.cube['orange'][2][1] and 'W' in self.cube['yellow'][1][0]:  # on orange-yellow edge c
            self.perform_moves("Y' B B")

        if 'W' in self.cube['orange'][2][1] and 'B' in self.cube['yellow'][1][0]:  # on orange-yellow edge BUT FLIPPEND c
            self.perform_moves("O B' O'")
        
        # White-Orange edge cases
        if 'O' in self.cube['white'][1][0] and 'W' in self.cube['orange'][0][1]:  # right place but flipped C
            self.perform_moves("O O Y G O' G'")
        
        if 'W' in self.cube['white'][2][1] and 'O' in self.cube['green'][0][1]:  # on white-green edge C
            self.perform_moves("G G Y' O O")
        
        if 'O' in self.cube['white'][2][1] and 'W' in self.cube['green'][0][1]:  # on white-green edge but flipped C
            self.perform_moves("G' O'")
        
        if 'W' in self.cube['white'][0][1] and 'O' in self.cube['blue'][2][1]:  # on white-blue edge C
            self.perform_moves("B B Y O O")
        
        if 'O' in self.cube['white'][0][1] and 'W' in self.cube['blue'][2][1]:  # on white-blue edge but flipped C
            self.perform_moves("B O")
        
        if 'W' in self.cube['white'][1][2] and 'O' in self.cube['red'][0][1]:  # on white-red edge C
            self.perform_moves("R R Y Y O O")
        
        if 'O' in self.cube['white'][1][2] and 'W' in self.cube['red'][0][1]:  # on white-red edge but flipped C
            self.perform_moves("R R Y' G O' G'")
        
        if 'O' in self.cube['orange'][1][0] and 'W' in self.cube['blue'][1][0]:  # on orange-blue edge C
            self.perform_moves("O")
        
        if 'W' in self.cube['orange'][1][0] and 'O' in self.cube['blue'][1][0]:  # on orange-blue edge but flipped C
            self.perform_moves("B Y O O B'")
        
        if 'O' in self.cube['orange'][2][1] and 'W' in self.cube['yellow'][1][0]:  # on orange-yellow edge 
            self.perform_moves("O O")
        
        if 'W' in self.cube['orange'][2][1] and 'O' in self.cube['yellow'][1][0]:  # on orange-yellow edge but flipped C
            self.perform_moves("Y G O' G'")
        
        if 'W' in self.cube['green'][1][0] and 'O' in self.cube['orange'][1][2]:  # on green-orange edge C
            self.perform_moves("O'")
        
        if 'O' in self.cube['green'][1][0] and 'W' in self.cube['orange'][1][2]:  # on green-orange edge but flipped C
            self.perform_moves("G' Y' O O G")
        
        if 'O' in self.cube['red'][1][2] and 'W' in self.cube['blue'][1][2]:  # on red-blue edge C
            self.perform_moves("R Y Y R' O O")
        
        if 'W' in self.cube['red'][1][2] and 'O' in self.cube['blue'][1][2]:  # on red-blue edge but flipped C
            self.perform_moves("B' Y O O B")
        
        if 'W' in self.cube['yellow'][0][1] and 'O' in self.cube['green'][2][1]:  # on yellow-green edge C
            self.perform_moves("G O' G'")
        
        if 'O' in self.cube['yellow'][0][1] and 'W' in self.cube['green'][2][1]:  # on yellow-green edge but flipped C
            self.perform_moves("Y' O")

        if 'O' in self.cube['red'][2][1] and 'W' in self.cube['yellow'][1][2]:  # on red-yellow edge C
            self.perform_moves("Y O O")
        
        if 'W' in self.cube['red'][2][1] and 'O' in self.cube['yellow'][1][2]:  # on red-yellow edge but flipped C
            self.perform_moves("Y' G O' G'")
        
        if 'O' in self.cube['blue'][0][1] and 'W' in self.cube['yellow'][2][1]:  # on blue-yellow edge C
            self.perform_moves("Y O O")
        
        if 'W' in self.cube['blue'][0][1] and 'O' in self.cube['yellow'][2][1]:  # on blue-yellow edge but flipped C
            self.perform_moves("B' O B")

        if 'O' in self.cube['green'][1][2] and 'W' in self.cube['red'][1][0]:  # on green-red edge C
            self.perform_moves("G Y' O O G'")
        
        if 'W' in self.cube['green'][1][2] and 'O' in self.cube['red'][1][0]:  # on green-red edge but flipped C
            self.perform_moves("R Y Y O O R'")

    def print_cube(self):
        for face, stickers in self.cube.items():
            print(f"Face: {face}")
            for row in stickers:
                print(" ".join(row))
            print()

# Main program
if __name__ == "__main__":
    cube = RubiksCube()
    cube.print_cube()
