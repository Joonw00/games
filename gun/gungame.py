import pygame   
import os    

#기본 초기화 부분(반드시 해야 함)
pygame.init()   #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height)) 


#화면 타이틀 설정
pygame.display.set_caption("팡팡") #게임 이름

#FPS
clock = pygame.time.Clock()

#1. 사용자 게임 초기화(배경,게임 이미지,좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)        #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")   #images폴더 위치 반환

#배경화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]        #스테이지의 높이에 캐릭터 두기 위해

#캐릭터 만들기
marine = pygame.image.load(os.path.join(image_path, "marine.png"))
marine_size = marine.get_rect().size
marine_width = marine_size[0]
marine_height = marine_size[1]
marine_x_pos = (screen_width / 2) - (marine_width / 2)
marine_y_pos = screen_height - stage_height - marine_height

marine_to_x = 0
marine_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한 번에 여러 발 발사 가능
weapons = []
#무기 이동 속도
weapon_speed = 10

#공 만들기(4개 크기에 대해 따로 처리)
slime_images = [
    pygame.image.load(os.path.join(image_path, "slime1.png")),
    pygame.image.load(os.path.join(image_path, "slime2.png")),
    pygame.image.load(os.path.join(image_path, "slime3.png")),
    pygame.image.load(os.path.join(image_path, "slime4.png"))]
#공 크기에 따른 최초 스피드
slime_speed_y = [-18, -15, -12, -9]      #index 0,1,2,3에 해당하는 값
#공들
slimes = []
#최초 발생하는 큰 공 추가   //딕셔너리 사용
slimes.append({
    "pos_x" : 50,   #공의 x좌표
    "pos_y" : 50,
    "img_idx": 0,    #공의 이미지 인덱스(??)
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y" : slime_speed_y[0]  #y최초 속도
})

#사라질 무기, 공 정보 저장 변수     //*****
weapon_to_remove = -1
slime_to_remove = -1

#폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 10
start_ticks = pygame.time.get_ticks()   #시작 시간 정의
game_result = "game over"


#이벤트 루프
running = True
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정

    #키보드,마우스 등 이벤트 처리
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:       
            running == False     

        if event.type == pygame.KEYDOWN:      
            if event.key == pygame.K_LEFT:
                marine_to_x -= marine_speed
            elif event.key == pygame.K_RIGHT:
                marine_to_x += marine_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = marine_x_pos + (marine_width/2) - (weapon_width / 2)
                weapon_y_pos = marine_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                marine_to_x = 0

    #3. 게임 캐릭터 위치 정의
    marine_x_pos += marine_to_x

    if marine_x_pos < 0:
        marine_x_pos = 0
    elif marine_x_pos > screen_width - marine_width:
        marine_x_pos = screen_width - marine_width

    #무기 위치 조정
    weapons = [[w[0], w[1]- weapon_speed ] for w in weapons]     #  무기 위치를 위로 올림
    #천장에 닿은 무기 삭제
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]       #연산자 우선순위***

    #공 위치 정의
    for slime_idx, slime_val in enumerate(slimes):          #**
        #slimes 리스트에 있는 것들을 하나씩 가져와서 현재 slime리스트의 몇 번 째인지 ,그 인덱스에 해당하는 값을 출력
        slime_pos_x = slime_val["pos_x"]
        slime_pos_y = slime_val["pos_y"]     
        slime_img_idx = slime_val["img_idx"]           
        slime_size = slime_images[slime_img_idx].get_rect().size        #표현 확인
        slime_width = slime_size[0]
        slime_height = slime_size[1]
        if slime_pos_x <= 0 or slime_pos_x > screen_width - slime_width:
            slime_val["to_x"] = slime_val["to_x"] * -1            #가로벽에 닿을 때 반대로 튕기기

        if slime_pos_y >= screen_height - stage_height - slime_height:
            slime_val["to_y"] = slime_val["init_spd_y"]         #스테이지에 튕겨서 올라가는 처리
        else:           #그 외 모든 경우에는 올라가는 속도 감소 (중력 설정)
            slime_val["to_y"] += 0.5
        slime_val["pos_x"] += slime_val["to_x"]
        slime_val["pos_y"] += slime_val["to_y"]        

    

    #4. 충돌 처리

    #캐릭터  rect 정보 업데이트
    marine_rect = marine.get_rect()
    marine_rect.left = marine_x_pos
    marine_rect.top = marine_y_pos

    #공과 캐릭터 충돌 처리
    for idx, val in enumerate(slimes):
        slime_pos_x = val["pos_x"]
        slime_pos_y = val["pos_y"]
        slime_img_idx = val["img_idx"]

        slime_rect = slime_images[slime_img_idx].get_rect()
        slime_rect.left = slime_pos_x
        slime_rect.top = slime_pos_y 
        if marine_rect.colliderect(slime_rect):
            running = False
            break

        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]
            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect_left = weapon_x_pos
            weapon_rect.top = weapon_y_pos
            #충돌 체크
            if weapon_rect.colliderect(slime_rect):
                weapon_to_remove = weapon_idx       #해당무기 없애기 위한 값 설정
                slime_to_remove = slime_idx

                #가장 작은 공이 아니라면 다음 단게의 공으로 나눠주기
                if slime_img_idx < 3:
                    #현재 공 크기 정보를 가지고 옴
                    slime_width = slime_rect.size[0]
                    slime_height = slime_rect.size[1]
                    #나눠진 공 정보
                    small_slime_rect = slime_images[slime_img_idx+1].get_rect()
                    small_slime_width = small_slime_rect.size[0]
                    small_slime_height = small_slime_rect.size[1]

                    #왼쪽으로 튕겨나가는  작은 공
                    slimes.append({
                        "pos_x" : slime_pos_x + (slime_width / 2) - (small_slime_width),   #공의 x좌표
                        "pos_y" : slime_pos_y + (slime_height / 2) - (small_slime_height),
                        "img_idx": slime_img_idx + 1,    #공의 이미지 인덱스(??)
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spd_y" : slime_speed_y[slime_img_idx + 1]  #y최초 속도
                    })
                    #오른쪽으로
                    slimes.append({
                        "pos_x" : slime_pos_x + (slime_width / 2) - (small_slime_width),
                        "pos_y" : slime_pos_y + (slime_height / 2) - (small_slime_height),
                        "img_idx": slime_img_idx + 1,    
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spd_y" : slime_speed_y[slime_img_idx + 1]
                    })
                    break
        else:
            continue        #계속 게임을 진행,,안쪽for문의 조건이 맞지 않으면 continue.바깥 쪽 for문이 계속 실행
        break   #안쪽 for문에서 break를 만나면 여기로 진입이 가능.2중 for문을 한번에 탈출

    #충돌된 공 or 무기 없애기
    if slime_to_remove > -1:        #****
        del slimes[slime_to_remove]
        slime_to_remove = -1
    if weapon_to_remove > -1:    
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    


    #5. 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:      #이렇게 표현 해도 되나??
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))       #blit순서에 따라 화면에 표현되는 우선순위 바뀜 

    for idx, val in enumerate(slimes):
        slime_pos_x = val["pos_x"]
        slime_pos_y = val["pos_y"]
        slime_img_idx = val["img_idx"]
        screen.blit(slime_images[slime_img_idx], (slime_pos_x,slime_pos_y))     #이해 필요

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(marine, (marine_x_pos, marine_y_pos))
    
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    #시간 초과 했다면
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False


    pygame.display.update()     #게임 화면을 다시 그리기(while문 내에서 반복되며)

#게임 오버 메시지
msg = game_font.render(game_result, True, (255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()     #화면에 반영

#잠시 대기
pygame.time.delay(500)      #2초 정도 대기

#pygame 종료
pygame.quit()