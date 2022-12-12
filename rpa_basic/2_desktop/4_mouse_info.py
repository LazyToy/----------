import pyautogui
pyautogui.FAILSAFE = False # 마우스를 중간에 귀퉁이 갔다놓아도 끝나지 않고 쭉 실행됨
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep을 적용
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)

# 자동화 중간에 자동화를 멈추고 싶다면 마우스를 양쪽 모서리 귀퉁이 어디든 갔다대면 된다.