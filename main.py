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
        pass

    def cross(self):
        # Solve the cross on one face
        pass

    def f2l(self):
        # Solve the first two layers
        pass

    def oll(self):
        # Orient the last layer
        pass

    def pll(self):
        # Permute the last layer
        pass

    def solve(self):
        # Solve the Rubik's Cube using CFOP method
        self.cross()
        self.f2l()
        self.oll()
        self.pll()

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
