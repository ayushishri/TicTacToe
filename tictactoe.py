class ttt:
    def __init__(self):
        self.T=[0 for i in range(0,9)]

    def analyzeBoard(self):
        board=0
        full=True
        for j in range(1,3,1):
            for i in range(0,3,1):
                if(self.T[i*3]==j and self.T[i*3+1]==j and self.T[i*3+2]==j):
                    board=j
                if(self.T[i]==j and self.T[i+3]==j and self.T[i+6]==j):
                    board=j
            for i in range(0,2,1):
                if (self.T[4]==j and self.T[i*2]==j and self.T[8-i*2]==j):
                    board=j
        for i in range(0,len(self.T),1):
            if (self.T[i]==0):
                full=False
        if full:
            board=3
        return board
    def genWinningMove(self,player):
        if ((self.analyzeBoard()==3) or (self.analyzeBoard()==-1) or (player>2 and player<1)):
            return -1
        j=player
        for i in range(0,3,1):
            if(self.T[i*3]==j and self.T[i*3+1]==j and self.T[i*3+2]==0):
                return (i*3+2)
            elif (self.T[i*3+1]==j and self.T[i*3+2]==j and self.T[i*3]==0):
                return i*3
            elif (self.T[i*3]==j and self.T[i*3+2]==j and self.T[i*3+1]==0):
                return (i*3+1)
            elif(self.T[i]==j and self.T[i+3]==j and self.T[i+6]==0):
                return (i+6)
            elif (self.T[i+3]==j and self.T[i+6]==j and self.T[i]==0):
                return i
            elif (self.T[i]==j and self.T[i+6]==j and self.T[i+3]==0):
                return i+3
        for i in range(0,2,1):
            if (self.T[4]==j and self.T[i*2]==j and self.T[8-i*2]==0):
                return 8-i*2
            elif (self.T[4]==j and self.T[i*2]==0 and self.T[8-i*2]==j):
                return i*2
            elif (self.T[4]==0 and self.T[i*2]==j and self.T[8-i*2]==j):
                return 4
        return -1
    def genNonLoser(self,player):
        if ((self.analyzeBoard()==3) or (self.analyzeBoard()==-1) or (player>2 and player<1)):
            return -1
        if (player==1):
            j=2
        elif(player==2):
            j=1
        for i in range(0,3,1):
            if(self.T[i*3]==j and self.T[i*3+1]==j and self.T[i*3+2]==0):
                return (i*3+2)
            elif (self.T[i*3+1]==j and self.T[i*3+2]==j and self.T[i*3]==0):
                return i*3
            elif (self.T[i*3]==j and self.T[i*3+2]==j and self.T[i*3+1]==0):
                return (i*3+1)
            elif(self.T[i]==j and self.T[i+3]==j and self.T[i+6]==0):
                return (i+6)
            elif (self.T[i+3]==j and self.T[i+6]==j and self.T[i]==0):
                return i
            elif (self.T[i]==j and self.T[i+6]==j and self.T[i+3]==0):
                return i+3
        for i in range(0,2,1):
            if (self.T[4]==j and self.T[i*2]==j and self.T[8-i*2]==0):
                return 8-i*2
            elif (self.T[4]==j and self.T[i*2]==0 and self.T[8-i*2]==j):
                return i*2
            elif (self.T[4]==0 and self.T[i*2]==j and self.T[8-i*2]==j):
                return 4
        return -1
    def genRandomMove(self,player):
        import random
        n_opens = 0
        for i in range(0,len(self.T),1):
            if self.T[i] == 0:
                n_opens = n_opens + 1
        if n_opens == 0:
            return -1
        else:
            while True:
                move = random.randint(0,8)
                if self.T[move] == 0:
                    return move

    def Move(self,x,player):
        if self.T[x] == 0:
            self.T[x]=player
            return True
        else:
            return False

    def copy(self,source):
        if len(self.T) != len(source.T):
            return False
        else:
            for i in len(self.T):
                self.T[i]=source.T[i]
            return True
