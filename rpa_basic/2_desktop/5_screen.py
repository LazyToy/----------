import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 22,27 44,162,241 #30A3F1

pixel = pyautogui.pixel(22,27)
print(pixel)

# print(pyautogui.pixelMatchesColor(22,27,(44,162,241)))
print(pyautogui.pixelMatchesColor(22,27,pixel))