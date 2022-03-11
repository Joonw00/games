import pygame

pygame.init()   #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#이벤트 루프
running = True  #게임이 진행 중인가?
while running:
    for event in pygame.event.get():        #pymgae을 쓰기 위해선 무조건 적어야 하는 부분(암기)
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생 하였는가?
            running == False                #게임이 진행중이 아님

#pygame 종료
pygame.quit()