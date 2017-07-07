
class Maze:
    def __init__(self, maze_file):
        self.data = []
        with open(maze_file, 'r') as maze_file:
            for line in maze_file:
                if not line.startswith('|'):
                    continue
                self.data.append([x for x in line.strip()])

        self.moves = []
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                moves = ''
                if self.data[i][j+1] == ' ':
                    moves += 'd'
                if self.data[i][j-1] == ' ':
                    moves += 'a'
                if self.data[i][j] == ' ':
                    moves += 's'
                if self.data[i-1][j] == ' ':
                    moves += 'w'
                

    def __str__(self):
        ret = ''
        for line in self.data:
            ret+= ''.join(line) + '\n'
        return ret
            
def main():
    m = Maze('tower.txt')
    print(m)

if __name__ == "__main__":
    main()
