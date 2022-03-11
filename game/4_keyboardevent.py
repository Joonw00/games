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

#캐릭터 불러오기
character = pygame.image.load("C:\\Users\\admin\\Desktop\\python\\python\\game\\char.png")
character_size = character.get_rect().size #이미지의 크기를 구해 옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos =   (screen_width / 2) - (character_width / 2)   #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height         #화면 세로 크기 가장 아래 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True  #게임이 진행 중인가?
while running:
    for event in pygame.event.get():        #pymgae을 쓰기 위해선 무조건 적어야 하는 부분(암기)
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생 하였는가?
            running == False                #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    #키가 눌러졌는 지확인
            if event.key == pygame.K_LEFT:  #캐릭터를 왼쪽으로
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:      #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    #경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    screen.blit(background, (0, 0))         #0,0은 왼쪽 맨 위   #blit으로 실제로 background 이미지를 실제로 그려줌,,배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  #캐릭터 그리기

    pygame.display.update()     #게임 화면을 다시 그리기(while문 내에서 반복되며)


#pygame 종료
pygame.quit()