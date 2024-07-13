class Chess:
    def __init__(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

class ChessBoard:
    def __init__(self):
        self.__grid=[[None for i in range(15)]for j in range(15)]
    def getGrid(self):
        return self.__grid
    def showBoard(self):
        for i in range(0,15,1):
            for j in range(0,15,1):
                if self.__grid[i][j]==None:
                    print("空",end="")
                elif self.__grid[i][j].getColor()=="white":
                    print("白",end="")
                else:
                    print("黑",end="")
            print()
#Austin very happy
class Player:
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
    def getName(self):
        return self.__name
    def getColor(self):
        return self.__color



class Referee:
    def __init__(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def __judgeRow(self,board):
        return "NO winner"

    def __judgeCol(self,board):
        return "NO winner"

    def __judgeTopLeftTriangle(self,board):
        return "NO winner"
    def __bottomRightTriangle(self, board):
        return "NO winner"

    def __bottomLeftTriangle(self,board):
        return "NO winner"

    def __judgeTopRightTriangle(self,board):
        return "NO winner"

    def judge(self,board):
        if self.__judgeRow(board)=="white win" or self.__judgeCol(board)=="white win" or self.__judgeTopLeftTriangle(board)=="white win" or self.__bottomRightTriangle(board)=="white win" or self.__bottomLeftTriangle(board)=="white win" or self.__judgeTopRightTriangle(board)=="white win":
            return "white win"
        elif self.__judgeRow(board)=="black win" or self.__judgeCol(board)=="black win" or self.__judgeTopLeftTriangle(board)=="black win" or self.__bottomRightTriangle(board)=="black win" or self.__bottomLeftTriangle(board)=="black win" or self.__judgeTopRightTriangle(board)=="black win":
            return "black win"
        else:
            return "NO winner"


class GameController:
    def start(self):
        lily = Player("Lily Sun", "white")
        tom = Player("Tom Cruise", "black")
        referee = Referee("john smith")
        c = ChessBoard()

        while True:
            #black first
            row=eval(input("black player,enter your row position"))
            col = eval(input("black player,enter your column position"))
            while tom.putDownChess(c,row,col)==False:
                row = eval(input("black player,already occupied,Re-enter your row position"))
                col = eval(input("black player,already occupied,Re-enter your column position"))
            c.showBoard()
            if referee.judge(c)=="black win":
                print("==========================Congratulation! Black Wins==================================")
                break
            # white then










# print(5/0)
# list=[5,6,7]
# print(list[1000])


# c=ChessBoard()
# lily=Player("Lily Sun","white")
# tom=Player("Tom Cruise","black")
#
# referee=Referee("join")
#
# # referee.judgeTopRightTriangle(c)
# referee.judge(c)
# print(tom.putDownChess(c,3,4))
# print(referee.judge(c))
# print(tom.putDownChess(c,3,5))
# print(referee.judge(c))
# print(tom.putDownChess(c,3,6))
# print(referee.judge(c))
# print(tom.putDownChess(c,3,7))
# print(referee.judge(c))
# print(tom.putDownChess(c,3,8))
# print(referee.judge(c))
# print(tom.putDownChess(c,3,9))
# print(referee.judge(c))
# print(tom.putDownChess(c,3,10))
# print(referee.judge(c))
# c.showBoard()

# print(tom.putDownChess(c,3,3))
# print(referee.judgeCol(c))
# print(lily.putDownChess(c,4,3))
# print(referee.judgeCol(c))
# print(tom.putDownChess(c,5,3))
# print(referee.judgeCol(c))
# print(tom.putDownChess(c,6,3))
# print(referee.judgeCol(c))
# print(tom.putDownChess(c,7,3))
# print(referee.judgeCol(c))
# print(tom.putDownChess(c,8,3))
# print(referee.judgeCol(c))
# print(tom.putDownChess(c,9,3))
# print(referee.judgeCol(c))

# print(tom.putDownChess(c,0,4))
# print(referee.judgeTopLeftTriangle(c))
# print(tom.putDownChess(c,1,3))
# print(referee.judgeTopLeftTriangle(c))
# print(tom.putDownChess(c,2,2))
# print(referee.judgeTopLeftTriangle(c))
# print(tom.putDownChess(c,3,1))
# print(referee.judgeTopLeftTriangle(c))
# print(tom.putDownChess(c,4,0))
# print(referee.judgeTopLeftTriangle(c))

# print(tom.putDownChess(c,7,0))
# print(referee.bottomLeftTriangle(c))
# print(tom.putDownChess(c,8,1))
# print(referee.bottomLeftTriangle(c))
# print(tom.putDownChess(c,9,2))
# print(referee.bottomLeftTriangle(c))
# print(tom.putDownChess(c,10,3))
# print(referee.bottomLeftTriangle(c))
# print(tom.putDownChess(c,11,4))
# print(referee.bottomLeftTriangle(c))
# c.showBoard()

# print(tom.putDownChess(c,0,5))
# print(referee.judgeTopRightTriangle(c))
# print(tom.putDownChess(c,1,6))
# print(referee.judgeTopRightTriangle(c))
# print(tom.putDownChess(c,2,7))
# print(referee.judgeTopRightTriangle(c))
# print(tom.putDownChess(c,3,8))
# print(referee.judgeTopRightTriangle(c))
# print(tom.putDownChess(c,4,9))
# print(referee.judgeTopRightTriangle(c))
# c.showBoard()








