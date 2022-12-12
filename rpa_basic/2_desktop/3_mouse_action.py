import pyautogui


# print(pyautogui.position())

# pyautogui.click(99, 25, duration=1) # 1초 동안 (99, 25) 좌표로 이동 후 마우스 클릭
# pyautogui.click() # click은 Down과 Up을 합친 함수
# pyautogui.mouseDown()  # 드래그 드랍을 할때 사용함
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(200, 300)
# pyautogui.mouseUp # 마우스 버튼 뗀 상태

pyautogui.sleep(3) # 3초 대기
# pyautogui.rightClick() # 마우스 우클릭
# pyautogui.middleClick() # 마우스 휠 클릭

# print(pyautogui.position())
pyautogui.moveTo(908, 161)
# pyautogui.drag(100, 0,) # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그
# pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 값 설정
# pyautogui.dragTo(1050, 230, duration=0.25) # 절대 좌표 기준으로 x 1050, y 230 으로 드래그

pyautogui.scroll(-300) # 양수이면 위 방향으로, 음수이면 아래방향으로 300 만큼 스크롤

