import sys
import heapdict



class Astar:
    def __init__(self,start):
        self.node = Node(start)
        self.queue = heapdict.heapdict()
        self.closed = []

    def space(self,node):
       
        moves = []

        j = node.arr.index(9)
       
        if (j-3) >= 0 :
            temp = []
            temp = node.arr.copy()
            x = temp[j-3]
            temp[j-3] = temp[j]
            temp[j] = x
            tempNode = Node(temp)
            if tempNode.arr not in self.closed:
                moves.append(tempNode)

        if (j + 3) < 9 :
            temp = []
            temp = node.arr.copy()
            x = temp[j+3]
            temp[j+3] = temp[j]
            temp[j] = x
            tempNode = Node(temp)
            if tempNode.arr not in self.closed:
                moves.append(tempNode)

        if (j - 1) >= 0:
            temp = []
            temp = node.arr.copy()
            x = temp[j-1]
            temp[j-1] = temp[j]
            temp[j] = x
            tempNode = Node(temp)
            if tempNode.arr not in self.closed:
                moves.append(tempNode)

        if (j + 1) < 9:
            temp = []
            temp = node.arr.copy()
            x = temp[j+1]
            temp[j + 1] = temp[j]
            temp[j] = x
            tempNode = Node(temp)
            if tempNode.arr not in self.closed:
                moves.append(tempNode)

        return moves

    def transition(self,node):
        x = self.space(node)

        for state in x:
            self.queue[state] = state.misplaced + node.gn

        temp = self.queue.popitem()[0]
        self.closed.append(temp.arr)
        return temp


   
    def move(self):

        x = self.transition(self.node)
        x.parent = self.node
        x.gn = self.node.gn + 1
        self.node = x


       
    def ifGoal(self):
        return self.node.arr == [1,2,3,
                                4,5,6,
                                7,8,9]

   


class Node:
    def __init__(self,arr):
        self.arr = arr
        self.misplaced = self.totalMisplaced(arr)
        self.parent = self
        self.gn = 0
       

    def totalMisplaced(self,arr):
        i = 1
        misplaced = 0
        for x in arr:
            if i != x:
                misplaced += 1

            i += 1

        return misplaced
                


def main():

    start = []
    for i in range(0,3):
      itemp = input()
      for x in itemp.split(' '):
        start.append(int(x))  

    print()
    pairs = 0

    for i in range(0,9):
        for j in range(i + 1,9):
            if j < 9 :
                if(start[j] < start[i]):
                    pairs += 1


    if pairs % 2 != 0:
        print("This configuration of the puzzle cannot be solved")
      
    else:
        temp = Astar(start)
        printa(temp.node.arr)

        while temp.ifGoal() == False:
            temp.move()
            printa(temp.node.arr)



def printa(arr):
    for i in range(1,10):
        print(arr[i-1],end = " ")
        if(i % 3 == 0):
            print()
       
    print()
       

if __name__ == "__main__":
    main()
