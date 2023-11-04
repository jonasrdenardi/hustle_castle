import pyautogui as pag
import time

poderInimigoIniX = 1033
poderInimigoFimX = 1266
poderInimigoIniY = 452
poderInimigoFimY = 497

posStart = 567, 897
corStart = 95, 184, 34
posConfPel = 919, 893

posIniTelaLutadores = 1691, 240
corIniTelaLutadores = 76, 187, 12

time.sleep(5)

# Iniciar arena
pag.moveTo(posStart[0], posStart[1], 1)
pag.click()
time.sleep(2)

# Confirmar pelotao
pag.moveTo(posConfPel[0], posConfPel[1], 1)
pag.click()
time.sleep(2)

while (pag.pixelMatchesColor(posIniTelaLutadores[0], posIniTelaLutadores[1], corIniTelaLutadores) == False):
    continue

pos1 = 924, 246
pos2 = 721, 497
pos3 = 1061, 496
pos4 = 557, 684
pos5 = 888, 686
pos6 = 1215, 686
pos7 = 350, 875
pos8 = 698, 878
pos9 = 1036, 879
pos10 = 1384, 875

corJaAtac = 96, 96, 96

posAtac = 1258, 882

posIniTelaFimLuta = 891, 962
corIniTelaFimLuta = 76, 187, 12

# Se não ataquei o 10 colocado en move e ataca
if pag.pixelMatchesColor(pos10[0], pos10[1], corJaAtac) == False:
    pag.moveTo(pos10[0], pos10[1], 1)
    pag.click()
    pag.moveTo(posAtac[0], posAtac[1], 1)
    pag.click()
    time.sleep(1)
    while (pag.pixelMatchesColor(posIniTelaFimLuta[0], posIniTelaFimLuta[1], corIniTelaFimLuta) == False):
        continue
    pag.moveTo(posIniTelaFimLuta[0], posIniTelaFimLuta[1], 1)
    pag.click()

time.sleep(10)
pag.moveTo(pos9[0], pos9[1], 1)

posIniTelaLutadoresEncerrado = 1661, 223
corIniTelaLutadoresEncerrado = 150, 8, 8

corJaAtacFora = 164, 161, 164




posFecharJanelaAtac = 1496, 155

# POS_INI_ATAQ = 1015, 609
# COR_INI_ATAQ = 110, 210, 23
# POS_FIM_ATAQ = 719, 686
# COR_FIM_ATAQ = 76, 187, 12
# POS_INI_ATAQ_ESG = 926, 636
# COR_INI_ATAQ_ESG = 255, 0, 0

# time.sleep(5)

# pag.moveTo(POS_INI_ATAQ[0], POS_INI_ATAQ[1], 1)

# count = 0

# while (True):

#     if pag.pixelMatchesColor(POS_INI_ATAQ_ESG[0], POS_INI_ATAQ_ESG[1], COR_INI_ATAQ_ESG):
#         break

#     if pag.pixelMatchesColor(POS_INI_ATAQ[0], POS_INI_ATAQ[1], COR_INI_ATAQ):
#         count += 1
#         pag.click(POS_INI_ATAQ[0], POS_INI_ATAQ[1])
#         pag.moveTo(POS_FIM_ATAQ[0], POS_FIM_ATAQ[1], 1)
#         print(count)
#     elif pag.pixelMatchesColor(POS_FIM_ATAQ[0], POS_FIM_ATAQ[1], COR_FIM_ATAQ):
#         pag.click(POS_FIM_ATAQ[0], POS_FIM_ATAQ[1])
#         pag.moveTo(POS_INI_ATAQ[0], POS_INI_ATAQ[1], 1)
