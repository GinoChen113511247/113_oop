import pygame

def update_ball(ball, screen_width, screen_height):
    # 更新位置
    ball['pos'][0] += ball['velocity'][0]
    ball['pos'][1] += ball['velocity'][1]

    # 檢查左右邊界，若碰到則反轉 x 軸速度
    if ball['pos'][0] - ball['radius'] <= 0 or ball['pos'][0] + ball['radius'] >= screen_width:
        ball['velocity'][0] = -ball['velocity'][0]

    # 檢查上下邊界，若碰到則反轉 y 軸速度
    if ball['pos'][1] - ball['radius'] <= 0 or ball['pos'][1] + ball['radius'] >= screen_height:
        ball['velocity'][1] = -ball['velocity'][1]

def draw_ball(ball):
    # add your code here
    

def main():
    # add your code here
    
    

    ball = {
        'screen': screen,
        'color': (255, 255, 255),       
        'radius': 20,
        'pos': [screen_width // 2, screen_height // 2],  # 初始位置在畫面中央
        'velocity': [3, 3]              
    }

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # add your code here
        

        # 更新球的位置及反彈邏輯
        update_ball(ball, screen_width, screen_height)
        draw_ball(ball)

        # add your code here
        

        clock.tick(60)

    # add your code here
    

if __name__ == "__main__":
    main()