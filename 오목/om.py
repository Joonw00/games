#시간제한, 턴 수 UI추가
#렌주 룰 추가해야 함
#ML 추가 시, win=0변수 추가해서 조건 설정 하면 될 듯
#게임 창과 따로, gui띄워서 무르기,기권,한수 쉼 기능 추가해볼 것

import pygame, sys
from pygame.locals import *
import rule
import let
#기본 초기화 부분(반드시 해야 함)
pygame.init()   #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 


#화면 타이틀 설정
pygame.display.set_caption("오목") #게임 이름

#FPS
clock = pygame.time.Clock()

#1. 사용자 게임 초기화(배경,게임 이미지,좌표, 속도, 폰트 등)
White = (255,255,255)
Black = (0,0,0)
brown = (153,102,0)
Radius = 20

stay = []   #돌들의 유지를 위해 선언
turn = 1 #처음에는 검은 색 차례

B_stone = []
W_stone = []

#이벤트 루프
running = True
while running:
    screen.fill(brown)
    dt = clock.tick(60)
    #추가할 것 : 화점 표시해야될 듯.. 격자 보니까 정신병 걸릴 거 같네
    for i in range(15):
        pygame.draw.line(screen, Black, (0, 40+40*i),(640,40+40*i), 3)
        pygame.draw.line(screen, Black, (40+40*i,0),(40+40*i,640), 3)

    #키보드,마우스 등 이벤트 처리
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:       
            running == False    
        #esc종료
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:      
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            crd = pygame.mouse.get_pos()
            x1 = crd[0]
            y1 = crd[1]
            x = let.adjx(x1)
            y = let.adjy(y1)
            #놓은 자리에 못놓게
            if [x,y] in stay:
                print("이미 놓은 자리 입니다")
                break
            #흑 차례 렌주룰
            if turn%2 == 1: 
                ren1 = rule.thth([x,y],B_stone,W_stone)
                ren2 = rule.B_six([x,y],B_stone)
            if ren1 == 1 or ren2 == 1:
                break
            stay.append([x,y])
            if turn%2 == 1:
                B_stone.append([x//40,y//40])
            else:
                W_stone.append([x//40,y//40])
            turn+=1
    #이미 놔진 돌들 유지하는 부분
    for i in range(len(stay)):
        x2 = stay[i][0]
        y2 = stay[i][1]
        if i%2 == 0:
            pygame.draw.circle(screen,Black,[x2,y2],Radius)
        else:
            pygame.draw.circle(screen,White,[x2,y2],Radius)
    #종료조건을 running == False 로 바꿔서 오류  제거 해야 할 듯
    rule.judge(B_stone,turn)
    rule.judge(W_stone,turn)


    pygame.display.update()

# 이거 왜 필요 했지???
# pygame.time.delay(2000)


#pygame 종료
pygame.quit()