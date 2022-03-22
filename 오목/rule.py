import pygame, sys
from pygame.locals import *

#종료 조건
def judge(stone,turn):
    stone.sort()
    for i in range(len(stone)):
        x = stone[i][0]
        y = stone[i][1]
        fiver(5,x,y,stone,turn)
        fived(5,x,y,stone,turn)
        fivedg(5,x,y,stone,turn)
        fiveu(5,x,y,stone,turn)
    return

#정확한 33의 정의는 아니지만, 정하기 나름이라 내가 편한 거로 정했음
def thth(cur,B,W): #33
    x = cur[0]//40
    y = cur[1]//40
    
    th3 = 0 #이게 2이상이면 33
    th4 = 0 #이게 2 이상이면 44.
    if [x+1,y] not in W and [x+2,y] not in W and [x+3,y] not in W and [x-1,y] not in W and [x-2,y] not in W and [x-3,y] not in W:
        line = 0    #한 줄에 같은게 몇 개 있는 지
        for i in range(1,4):
            i = int(i)
            if [x+i,y] in B:
                line+=1
            if [x-i,y] in B:
                line+=1
        if line == 2:
            th3+=1
        elif line == 3:
            th4+=1
    if [x,y+1] not in W and [x,y+2] not in W and [x,y+3] not in W and [x,y-1] not in W and [x,y-2] not in W and [x,y-3] not in W:
        line = 0
        for i in range(1,4):
            i = int(i)
            if [x,y+i] in B:
                line+=1
            if [x,y-i] in B:
                line+=1
        print(line)
        if line == 2:
            th3+=1
        elif line == 3:
            th4+=1
    if [x+1,y+1] not in W and [x+2,y+2] not in W and [x+3,y+3] not in W and [x-1,y-1] not in W and [x-2,y-2] not in W and [x-3,y-3] not in W:
        line = 0
        for i in range(1,4):
            i = int(i)
            if [x+i,y+i] in B:
                line+=1
            if [x-i,y-i] in B:
                line+=1
        if line == 2:
            th3+=1
        elif line == 3:
            th4+=1
    if [x+1,y-1] not in W and [x+2,y-2] not in W and [x+3,y-3] not in W and [x-1,y+1] not in W and [x-2,y+2] not in W and [x-3,y+3] not in W:
        line = 0
        for i in range(1,4):
            i = int(i)
            if [x+i,y-i] in B:
                line+=1
            if [x-i,y+i] in B:
                line+=1
        if line == 2:
            th3+=1
        elif line == 3:
            th4+=1
    if th3>=2:
        print("3x3 입니다.")
        return 1
    elif th4>=2:
        print("4x4 입니다.")
        return 1
    return 0


def B_six(cur,stone):    #6목
    x = cur[0]//40
    y = cur[1]//40
    if [x+1,y+1] in stone and [x+2,y+2] in stone and [x-1,y-1] in stone and [x-2,y-2] in stone and [x-3,y-3] in stone:
        print("6목 입니다")
        return 1
    if [x+1,y+1] in stone and [x+2,y+2] in stone and [x-1,y-1] in stone and [x-2,y-2] in stone and [x+3,y+3] in stone:
        print("6목 입니다")
        return 1
    if [x+1,y] in stone and [x+2,y] in stone and [x-1,y] in stone and [x-2,y] in stone and [x-3,y] in stone:
        print("6목 입니다")
        return 1
    if [x+1,y] in stone and [x+2,y] in stone and [x-1,y] in stone and [x-2,y] in stone and [x+3,y] in stone:
        print("6목 입니다")
        return 1
    if [x+1,y-1] in stone and [x+2,y-2] in stone and [x-1,y+1] in stone and [x-2,y+2] in stone and [x-3,y+3] in  stone:
        print("6목 입니다")
        return 1
    if [x+1,y-1] in stone and [x+2,y-2] in stone and [x-1,y+1] in stone and [x-2,y+2] in stone and [x+3,y-3] in  stone:
        print("6목 입니다")
        return 1
    return 0






#5개가 연속해있는 지 판단(우측)
def fiver(n,x,y,stone,turn):
    if n == 1: 
        if turn%2 == 1:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()   #이거 바꿔 줘야 됨(메인에서 업데이트 에러 뜸)
    if [x+1,y] in stone:
        fiver(n-1,x+1,y,stone,turn)
    return

def fived(n,x,y,stone,turn):
    if n == 1: 
        if turn%2 == 1:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()    
        return
    if [x,y+1] in stone:
        fived(n-1,x,y+1,stone,turn)
    return

def fivedg(n,x,y,stone,turn):
    if n == 1: 
        if turn%2 == 1:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()
        return
    if [x+1,y+1] in stone:
        fivedg(n-1,x+1,y+1,stone,turn)
    return
def fiveu(n,x,y,stone,turn):
    if n == 1: 
        if turn%2 == 1:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()
        return
    if [x+1,y-1] in stone:
        fiveu(n-1,x+1,y-1,stone,turn)
    return