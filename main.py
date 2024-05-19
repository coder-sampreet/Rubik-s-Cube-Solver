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

    def white_cross(self):
        #complete the white cross using beginner's method

# if already crossed then skip
        if 'W' in self.cube['white'][2][1] and 'G' in self.cube['green'][0][1]:
            pass
        if 'W' in self.cube['white'][1][0] and 'O' in self.cube['orange'][0][1]:
            pass
        if 'W' in self.cube['white'][1][2] and 'R' in self.cube['red'][0][1]:
            pass
        if 'W' in self.cube['white'][0][1] and 'B' in self.cube['blue'][2][1]:
            pass

# for white green edge

        if 'G' in self.cube['white'][2][1] and 'W' in self.cube['green'][0][1]: #right place but fliped
            print("G2  Y  R  G'  R'")
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('green')
            cube.rotate_face_counter_clockwise('red')

        if 'W' in self.cube['white'][1][2] and 'G' in self.cube['red'][0][1]: # on white red edge
            print("R'2  Y'  G2")
            cube.rotate_face_counter_clockwise('red')
            cube.rotate_face_counter_clockwise('red')
            cube.rotate_face_counter_clockwise('yellow')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'G' in self.cube['white'][1][2] and 'W' in self.cube['red'][0][1]: # on white red edge but flipped
            print("R' G'")
            cube.rotate_face_counter_clockwise('red')
            cube.rotate_face_counter_clockwise('green')

        if 'W' in self.cube['white'][1][0] and 'G' in self.cube['orange'][0][1]: # on white orange edge
            print("O2  Y  G2")
            cube.rotate_face_clockwise('orange')
            cube.rotate_face_clockwise('orange')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'G' in self.cube['white'][1][0] and 'W' in self.cube['orange'][0][1]: # on white orange edge but flipped
            print("O  G")
            cube.rotate_face_clockwise('orange')
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['white'][0][1] and 'G' in self.cube['blue'][2][1]: # on white blue edge
            print("B2  Y2  G2")
            cube.rotate_face_clockwise('blue')
            cube.rotate_face_clockwise('blue')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'G' in self.cube['white'][0][1] and 'W' in self.cube['blue'][2][1]: # on white blue edge but fliped
            print("B2  Y'  R   G'  R'")
            cube.rotate_face_clockwise('blue')
            cube.rotate_face_clockwise('blue')
            cube.rotate_face_counter_clockwise('yellow')
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('green')
            cube.rotate_face_counter_clockwise('red')

        if 'G' in self.cube['green'][1][2] and 'W' in self.cube['red'][1][0]: # on green red edge
            print("G'")
            cube.rotate_face_counter_clockwise('green')

        if 'W' in self.cube['green'][1][2] and 'G' in self.cube['red'][1][0]: # on green red edge but flipped
            print("R'  Y'  R  G2")
            cube.rotate_face_counter_clockwise('red')
            cube.rotate_face_counter_clockwise('yellow')
            cube.rotate_face_clockwise('red')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')
        
        if 'G' in self.cube['green'][1][0] and 'W' in self.cube['orange'][1][2]: # on green orange edge
            print("G")
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['green'][1][0] and 'G' in self.cube['orange'][1][2]: # on green orange edge but flipped
            print("O  Y  O'  G2")
            cube.rotate_face_clockwise('orange')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_counter_clockwise('orange')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')
            
        if 'G' in self.cube['green'][2][1] and 'W' in self.cube['yellow'][0][1]: # on green yellow edge
            print("G2")
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['green'][2][1] and 'G' in self.cube['yellow'][0][1]: # on green yellow edge but flipped
            print("Y  R  G'  R'")
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('green')
            cube.rotate_face_counter_clockwise('red')

        if 'G' in self.cube['red'][2][1] and 'W' in self.cube['yellow'][1][2]: # on red yellow edge
            print("Y'  G2")
            cube.rotate_face_counter_clockwise('yellow')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')
        
        if 'W' in self.cube['red'][2][1] and 'G' in self.cube['yellow'][1][2]: # on red yellow edge but flipped
            print("R  G'  R'")
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('green')
            cube.rotate_face_counter_clockwise('red')

        if 'G' in self.cube['orange'][2][1] and 'W' in self.cube['yellow'][1][0]: # on orange yellow edge
            print("Y  G2")
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['orange'][2][1] and 'G' in self.cube['yellow'][1][0]: # on orange yellow edge but flipped
            print("O'  G  O")
            cube.rotate_face_counter_clockwise('orange')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('orange')

        if 'G' in self.cube['blue'][0][1] and 'W' in self.cube['yellow'][2][1]: # on blue yellow edge
            print("Y2  G2")
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['blue'][0][1] and 'G' in self.cube['yellow'][2][1]: # on blue yellow edge but flipped
            print("Y'  R  G'  R'")
            cube.rotate_face_counter_clockwise('yellow')
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('green')
            cube.rotate_face_counter_clockwise('red')

        if 'G' in self.cube['red'][1][2] and 'W' in self.cube['blue'][1][2]: # on red blue edge
            print("R  Y'  R'  G2")
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('yellow')
            cube.rotate_face_counter_clockwise('red')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['red'][1][2] and 'G' in self.cube['blue'][1][2]: # on red blue edge but flipped
            print("R2  G'  R'2")
            cube.rotate_face_clockwise('red')
            cube.rotate_face_clockwise('red')
            cube.rotate_face_counter_clockwise('green')
            cube.rotate_face_counter_clockwise('red')
            cube.rotate_face_counter_clockwise('red')

        if 'G' in self.cube['orange'][1][0] and 'W' in self.cube['blue'][1][0]: # on orange blue edge
            print("O'  Y  O  G2")
            cube.rotate_face_counter_clockwise('orange')
            cube.rotate_face_clockwise('yellow')
            cube.rotate_face_clockwise('orange')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('green')

        if 'W' in self.cube['orange'][1][0] and 'G' in self.cube['blue'][1][0]: # on orange blue edge but flipped
            print("O'2  G  O2")
            cube.rotate_face_counter_clockwise('orange')
            cube.rotate_face_counter_clockwise('orange')
            cube.rotate_face_clockwise('green')
            cube.rotate_face_clockwise('orange')
            cube.rotate_face_clockwise('orange')


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
