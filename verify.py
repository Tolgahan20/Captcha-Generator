# importing modules
from captcha.image import ImageCaptcha
import random

# creating the height and with of the image box
image = ImageCaptcha(width=200, height=90)

# assigning letters and numbers to a list to randomly select the captcha
letters = "abcdefghijklmnoprlstuvyzxABCDEFGHIJKLMNOPRSTUVYZX0123456789"
captcha_text = ""

# for loop to select random characters for captcha
for i in range(8):
    captcha_text += random.choice(letters)


data = image.generate(captcha_text)

image.write(captcha_text, 'CAPTCHA.png')
