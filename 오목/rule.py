import pygame, sys
from pygame.locals import *
#종료 조건
def judge(stone):
    stone.sort()
    for i in range(len(stone)):
        x = stone[i][0]
        y = stone[i][1]
        fiver(5,x,y,stone)
        fived(5,x,y,stone)
        fivedg(5,x,y,stone)
        fiveu(5,x,y,stone)
    return

#5개가 연속해있는 지 판단(우측)
def fiver(n,x,y,stone):
    if n == 1: 
        if len(stone)%2 == 0:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()   #이거 바꿔 줘야 됨(메인에서 업데이트 에러 뜸)
    if [x+1,y] in stone:
        fiver(n-1,x+1,y,stone)
    return

def fived(n,x,y,stone):
    if n == 1: 
        if len(stone)%2 == 0:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()    
        return
    if [x,y+1] in stone:
        fived(n-1,x,y+1,stone)
    return

def fivedg(n,x,y,stone):
    if n == 1: 
        if len(stone)%2 == 0:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()
        return
    if [x+1,y+1] in stone:
        fivedg(n-1,x+1,y+1,stone)
    return
def fiveu(n,x,y,stone):
    if n == 1: 
        if len(stone)%2 == 0:
            print("백이 승리했습니다.")
        else:
            print("흑이 승리했습니다.")
        pygame.quit()
        return
    if [x+1,y-1] in stone:
        fiveu(n-1,x+1,y-1,stone)
    return