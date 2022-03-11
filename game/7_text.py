import pygame

pygame.init()   #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#FPS
clock = pygame.time.Clock()

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

#이동 속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("C:\\Users\\admin\\Desktop\\python\\python\\game\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos =   (screen_width / 2) - (enemy_width / 2)   
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)       

#폰트 정의
game_font = pygame.font.Font(None, 40)      #폰트 객체 생성(폰트,크기)
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks()       #현재 tick 정보를 받아 옴


#이벤트 루프
running = True  #게임이 진행 중인가?
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정

    #print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():        #pymgae을 쓰기 위해선 무조건 적어야 하는 부분(암기)
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생 하였는가?
            running == False                #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    #키가 눌러졌는 지확인
            if event.key == pygame.K_LEFT:  #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:      #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt            #????프레임이 달라져도 이동속도는 동일하게 함

    #경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):        # 사각형 기준으로 충돌이 있었는 지를 확인하는 함수
        print("충돌했어요")
        running = False


    
    screen.blit(background, (0, 0))         #0,0은 왼쪽 맨 위   #blit으로 실제로 background 이미지를 실제로 그려줌,,배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  #캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))              #적 그리기

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000           #?????경과시간을 1000으로 나눠서 초 단위로 표시(원래는 ms)

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))      #실제로 글자를 그림
    #시간, True, 글자 색상
    screen.blit(timer, (10, 10))

    #시간이0이하면 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False


    pygame.display.update()     #게임 화면을 다시 그리기(while문 내에서 반복되며)

#잠시 대기
pygame.time.delay(2000)      #2초 정도 대기


#pygame 종료
pygame.quit()