from python_imagesearch.imagesearch import imagesearch
import pyautogui

IS_THE_END = True
start = str(input("Do you want to start? : "))
if start == "y":

    while(IS_THE_END):
        try:
            position = pyautogui.locateOnScreen('sign1.png', confidence=0.9)

            print(f"Position: {position[0]}, {position[1]}")
            pyautogui.click(position)

            print("[+++] Clicked")

        except pyautogui.ImageNotFoundException:
            print("Image not Found :( )")
            IS_THE_END = False


else:
    print("Goodbye ")