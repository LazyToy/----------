import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("123456")
# pyautogui.write("NadoCoding", interval=1)
# pyautogui.write("나도코딩") # 한글은 출력이 안됨

# pyautogui.write(["t","e","s","t","left","left","right","1","a","enter"],interval=0.25)
# # 차례로 적고 왼족 방향키 2번 오른쪽 방향키 1번 나머지 적고 enter 까지 입력 


# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.press("shift") # shift 키를 뗀다

# 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl 누르고 > alt 누르고 > shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고
pyautogui.hotkey("ctrl", "a")

import pyperclip
pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")  # 클립도느에 있는 내용르 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 자동화 프로그램 종료
# window : ctrl + alt + del