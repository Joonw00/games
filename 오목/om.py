import pygame, sys
from pygame.locals import *
#from rule import *   

#다른 모듈에 옮길 부분,귀찮다
def prog(turn,x,y):
    if turn%2 == 1:   #검은 색 차례일 때
        pygame.draw.circle(screen,Black,[x,y],Radius)
    elif turn%2 == 0:
        pygame.draw.circle(screen,White,[x,y],Radius)
def adjx(x):
    if x%40 <= 20:
        a = x%40
        x-=a
        return x
    elif x%40 > 20:
        a = x%40
        x-=a-40
        return x

def adjy(y):
    if y%40 <= 20:
        a = y%40
        y-=a
        return y
    elif y%40 > 20:
        a = y%40
        y-=a-40
        return y

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
        #개발 편의 용으로 넣은 거
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:      
                pygame.quit()  
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            crd = pygame.mouse.get_pos()
            x1 = crd[0]
            y1 = crd[1]
            x = adjx(x1)
            y = adjy(y1)
            stay.append([x,y])

            turn+=1
    #이미 놔진 돌들 유지하는 부분
    for i in range(len(stay)):
        x2 = stay[i][0]
        y2 = stay[i][1]
        if i%2 == 0:
            pygame.draw.circle(screen,Black,[x2,y2],Radius)
        else:
            pygame.draw.circle(screen,White,[x2,y2],Radius)

    pygame.display.update()

#잠시 대기
pygame.time.delay(2000)


#pygame 종료
pygame.quit()