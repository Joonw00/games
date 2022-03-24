#할 것들 목록
#시간제한, 턴 수 UI추가
#게임 창과 따로, gui띄워서 무르기,기권,한수 쉼 기능 추가 해 볼 것
#상수를 너무 많이 사용했음//공통되는 상수들 변수로 처리해 줄 것
#강화학습이용 AI 구현

#오류내역
#게임 끝날 때 마지막 돌 왜 안보이냐

import pygame, sys
from pygame.locals import *
import rule
import let

#초기화
pygame.init()

#화면 크기 설정
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 


#화면 타이틀 설정
pygame.display.set_caption("오목")

#FPS
clock = pygame.time.Clock()

#1. 변수 초기화
White = (255,255,255)
Black = (0,0,0)
brown = (153,102,0)
Radius = 20
game_font = pygame.font.Font(None, 40) 
start_ticks = pygame.time.get_ticks()
limit_time = 31 #시간 제한, 31이 보기 예쁨

stay = []   #돌들의 유지를 위해 선언
turn = 1 #처음에는 검은 색 차례

B_stone = []
W_stone = []

#언젠가 적용할 강화학습
win=0

#이벤트 루프
running = True
while running:
    screen.fill(brown)
    dt = clock.tick(60)
    #타이머 구현
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(limit_time-elapsed_time)), True, (255,255,255))
    screen.blit(timer, (5, 10))

    #추가할 것 : 그래픽 상향 좀
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
            start_ticks = pygame.time.get_ticks() #타이머 초기화
            crd = pygame.mouse.get_pos()
            x1 = crd[0]
            y1 = crd[1]
            x = let.adjx(x1)
            y = let.adjy(y1)
            #놓은 자리에 못놓게
            if [x,y] in stay:
                print("이미 놓은 자리 입니다")
                break
            #흑 차례에 렌주룰
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
    #돌 이미지 처리
    for i in range(len(stay)):
        x2 = stay[i][0]
        y2 = stay[i][1]
        if i%2 == 0:
            pygame.draw.circle(screen,Black,[x2,y2],Radius)
        else:
            pygame.draw.circle(screen,White,[x2,y2],Radius)

    #시간 패
    if elapsed_time > 31:
        rule.game_end((turn+1)%2,stay)
        start_ticks = pygame.time.get_ticks()
    #렌주룰 및 승리여부 판단
    rule.judge(B_stone,turn,stay)
    #이거 안쓰면 game_end함수 오토콜됨!! 1시간동안 찾았네
    if len(stay) == 0:
        B_stone.clear()
        W_stone.clear()
    rule.judge(W_stone,turn,stay)
    if len(stay) == 0:
        B_stone.clear()
        W_stone.clear()

    pygame.display.update()

#없어도 됨
pygame.time.delay(2000)


#pygame 종료
pygame.quit()