#렌주룰 따로 모듈 파서 분리하는 게 깔끔할 듯, 코드 너무 길다
import pygame, sys
from pygame.locals import *

#종료 조건
def judge(stone,turn,stay):
    stone.sort()
    for i in range(len(stone)):
        x = stone[i][0]
        y = stone[i][1]
        fiver(5,x,y,stone,turn,stay)
        fived(5,x,y,stone,turn,stay)
        fivedg(5,x,y,stone,turn,stay)
        fiveu(5,x,y,stone,turn,stay)
    return

#정확한 33의 정의는 아니지만, 정하기 나름이라 내가 편한 거로 정했음

#코드 정리 할 것
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

def game_end(winner,stay):
    if winner == 1:
        print("백이 승리했습니다")
    elif winner == 0:
        print("흑이 승리했습니다.")
    #결과 저장
    f = open("games\\오목\\game_data.txt",'a')
    f.write("{0}\n".format(stay))
    f.close()

    #게임 초기화 시키고 다시 시작
    stay.clear()
    return

#5개가 연속해있는 지 판단(우측)
def fiver(n,x,y,stone,turn,stay):
    if n == 1: 
        game_end(turn%2,stay)
        return
    if [x+1,y] in stone:
        fiver(n-1,x+1,y,stone,turn,stay)
    return

def fived(n,x,y,stone,turn,stay):
    if n == 1: 
        game_end(turn%2,stay) 
        return
    if [x,y+1] in stone:
        fived(n-1,x,y+1,stone,turn,stay)
    return

def fivedg(n,x,y,stone,turn,stay):
    if n == 1: 
        game_end(turn%2,stay)
        return
    if [x+1,y+1] in stone:
        fivedg(n-1,x+1,y+1,stone,turn,stay)
    return
def fiveu(n,x,y,stone,turn,stay):
    if n == 1: 
        game_end(turn%2,stay)
        return
    if [x+1,y-1] in stone:
        fiveu(n-1,x+1,y-1,stone,turn,stay)
    return