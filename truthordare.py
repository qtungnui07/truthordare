import pygame
import random
import sys
import subprocess

pygame.init()

# Setup
window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("TRUTH OR DARE")
running = True
color_background = (59, 66, 82)

# Music
pygame.mixer.music.load('Playlist.mp3')
pygame.mixer.music.play(-1)

# Font
font = pygame.font.Font('MinecraftRegular-Bmg3.ttf', 32)
font_vietnamese = pygame.font.Font('SVN-Arial Bold.ttf', 24)

# Button properties
button_color = (255, 255, 255)
button_text_color = (0, 0, 0)

# Sentences
sentences = []

# Define buttons
buttons = [
    {'rect': pygame.Rect(290, 70, 200, 50), 'text': 'Import data'},
    {'rect': pygame.Rect(130, 140, 50, 50), 'text': '1'},
    {'rect': pygame.Rect(230, 140, 50, 50), 'text': '2'},
    {'rect': pygame.Rect(330, 140, 50, 50), 'text': '3'},
    {'rect': pygame.Rect(430, 140, 50, 50), 'text': '4'},
    {'rect': pygame.Rect(530, 140, 50, 50), 'text': '5'},
    {'rect': pygame.Rect(630, 140, 50, 50), 'text': '6'}
]

# Draw buttons function
def draw_buttons():
    for button in buttons:
        pygame.draw.rect(screen, button_color, button['rect'])
        button_text = font.render(button['text'], True, button_text_color)
        screen.blit(button_text, (button['rect'].x + 10, button['rect'].y + 10))

# Function to import data
def import_data():
    global sentences
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            sentences = file.readlines()
        random.shuffle(sentences)
    except FileNotFoundError:
        print("Error: 'data.txt' file not found.")

# Function to show sentences
def show_sentences(button_index):
    global sentences
    if button_index is not None and button_index < len(sentences):
        sentence = sentences[button_index].strip()
        sentence_text = font_vietnamese.render(sentence, True, (255, 255, 255))
        text_rect = sentence_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
        screen.blit(sentence_text, text_rect)
# Main loop
current_question_index = None  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(buttons):
                if button['rect'].collidepoint(event.pos):
                    if button['text'] == 'Import data':
                        subprocess.Popen(['notepad.exe', 'data.txt'])
                        import_data()
                    else:
                        if len(sentences)>0:

	                        if current_question_index is not None:
	                            del sentences[current_question_index]  
	                        current_question_index = i  
    screen.fill(color_background)
    draw_buttons()

    if current_question_index is not None and current_question_index < len(sentences):
        show_sentences(current_question_index)

    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()
