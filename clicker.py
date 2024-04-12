import pyautogui as pg, time as tm
# Wait 10sec to open the game
tm.sleep(10)
# Click every 3 seconds to farm experience
for i in range(200):
    pg.click()
    tm.sleep(3)

