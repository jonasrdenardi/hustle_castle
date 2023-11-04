import pyautogui as pag
import time

POS_INI_ATAQ = 1015, 609
COR_INI_ATAQ = 110, 210, 23
POS_FIM_ATAQ = 719, 686
COR_FIM_ATAQ = 76, 187, 12
POS_INI_ATAQ_ESG = 926, 636
COR_INI_ATAQ_ESG = 255, 0, 0

time.sleep(5)

pag.moveTo(POS_INI_ATAQ[0], POS_INI_ATAQ[1], 1)

count = 0

while (True):

    if pag.pixelMatchesColor(POS_INI_ATAQ_ESG[0], POS_INI_ATAQ_ESG[1], COR_INI_ATAQ_ESG):
        break

    if pag.pixelMatchesColor(POS_INI_ATAQ[0], POS_INI_ATAQ[1], COR_INI_ATAQ):
        count += 1
        pag.click(POS_INI_ATAQ[0], POS_INI_ATAQ[1])
        pag.moveTo(POS_FIM_ATAQ[0], POS_FIM_ATAQ[1], 1)
        print(count)
    elif pag.pixelMatchesColor(POS_FIM_ATAQ[0], POS_FIM_ATAQ[1], COR_FIM_ATAQ):
        pag.click(POS_FIM_ATAQ[0], POS_FIM_ATAQ[1])
        pag.moveTo(POS_INI_ATAQ[0], POS_INI_ATAQ[1], 1)
