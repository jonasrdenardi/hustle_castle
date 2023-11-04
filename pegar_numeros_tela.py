import pyautogui
from PIL import Image
import pytesseract
import pytesseract
import time
import pyocr

# time.sleep(3)

# # Captura a região da tela desejada
# x, y, width, height = 763, 334, 143, 28  # Substitua pelos valores da sua região
# screenshot = pyautogui.screenshot(region=(x, y, width, height))

# # Salva a captura em um arquivo temporário
# screenshot.save('screenshot.png')

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

# Carrega a imagem usando o Pillow (PIL)
image = Image.open('screenshot.png')
numbers = extract_numbers_from_image(image)

print("Números extraídos:", numbers)