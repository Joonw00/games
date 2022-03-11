import pygame

pygame.init()   #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#배경 이미지 불러 오기
background = pygame.image.load("C:\\Users\\admin\\Desktop\\python\\python\\game\\background.png")   #탈출문자 때문에 \두개씩 입력or/로 교체

#이벤트 루프
running = True  #게임이 진행 중인가?
while running:
    for event in pygame.event.get():        #pymgae을 쓰기 위해선 무조건 적어야 하는 부분(암기)
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생 하였는가?
            running == False                #게임이 진행중이 아님
    

    #screen.fill((0, 0, 255))       ,,이렇게 설정 할 수도 있음
    screen.blit(background, (0, 0))         #0,0은 왼쪽 맨 위   #blit으로 실제로 background 이미지를 실제로 그려줌,,배경 그리기
    pygame.display.update()     #게임 화면을 다시 그리기(while문 내에서 반복되며)


#pygame 종료
pygame.quit()