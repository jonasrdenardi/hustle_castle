import pyautogui
import keyboard
import time
import pyocr
from PIL import Image
from io import BytesIO

# Configuração do pyocrp
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("Nenhuma ferramenta OCR disponível")
    exit(1)
tool = tools[0]  # Use a primeira ferramenta OCR disponível

def extract_numbers_from_image(image):
    extracted_text = tool.image_to_string(
        image,
        lang='eng',  # Defina o idioma, por exemplo, 'eng' para inglês
        builder=pyocr.builders.DigitBuilder()
    )
    return [int(word) for word in extracted_text.split() if word.isdigit()]

print("Pressione a tecla 'P' para extrair os números da imagem.")
print("Pressione a tecla 'Esc' para sair do programa.")

poderInimigoIniX = 1033
poderInimigoFimX = 1266
poderInimigoIniY = 452
poderInimigoFimY = 497
width = poderInimigoFimX - poderInimigoIniX
height = poderInimigoFimY - poderInimigoIniY

while True:
    if keyboard.is_pressed('p'):
        screenshot = pyautogui.screenshot(region=(poderInimigoIniX, poderInimigoIniY, width, height))
        screenshot_bytes = BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_pil = Image.open(screenshot_bytes)
        screenshot_pil.save("imagem.png")
        numbers = extract_numbers_from_image(screenshot_pil)
        print("Números extraídos:", numbers)
        time.sleep(3)

    if keyboard.is_pressed('esc'):
        print("Programa encerrado.")
        break
