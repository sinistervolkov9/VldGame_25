# --- Screen ---

RES = WIDTH, HEIGHT = 600, 400  # 1920, 1080  1366, 768  900, 500 || # 600, 400
FPS = 60  # 60

BASE_RES = (1920, 1080)

SCREEN_POS = {
    "tl": (0, 0),  # Top Left
    "tl01": (WIDTH // 8, 0),
    "tl02": (2 * WIDTH // 8, 0),
    "tl03": (3 * WIDTH // 8, 0),
    "tc": (4 * WIDTH // 8, 0),
    "tr03": (5 * WIDTH // 8, 0),
    "tr02": (6 * WIDTH // 8, 0),
    "tr01": (7 * WIDTH // 8, 0),
    "tr": (WIDTH, 0),  # Top Right

    "tl1": (0, HEIGHT // 8),
    "tl11": (WIDTH // 8, HEIGHT // 8),
    "tl12": (2 * WIDTH // 8, HEIGHT // 8),
    "tl13": (3 * WIDTH // 8, HEIGHT // 8),
    "tc1": (4 * WIDTH // 8, HEIGHT // 8),
    "tr13": (5 * WIDTH // 8, HEIGHT // 8),
    "tr12": (6 * WIDTH // 8, HEIGHT // 8),
    "tr11": (7 * WIDTH // 8, HEIGHT // 8),
    "tr1": (WIDTH, HEIGHT // 8),

    "tl2": (0, 2 * HEIGHT // 8),
    "tl21": (WIDTH // 8, 2 * HEIGHT // 8),
    "tl22": (2 * WIDTH // 8, 2 * HEIGHT // 8),
    "tl23": (3 * WIDTH // 8, 2 * HEIGHT // 8),
    "tc2": (4 * WIDTH // 8, 2 * HEIGHT // 8),
    "tr23": (5 * WIDTH // 8, 2 * HEIGHT // 8),
    "tr22": (6 * WIDTH // 8, 2 * HEIGHT // 8),
    "tr21": (7 * WIDTH // 8, 2 * HEIGHT // 8),
    "tr2": (WIDTH, 2 * HEIGHT // 8),

    "tl3": (0, 3 * HEIGHT // 8),
    "tl31": (WIDTH // 8, 3 * HEIGHT // 8),
    "tl32": (2 * WIDTH // 8, 3 * HEIGHT // 8),
    "tl33": (3 * WIDTH // 8, 3 * HEIGHT // 8),
    "tc3": (4 * WIDTH // 8, 3 * HEIGHT // 8),
    "tr33": (5 * WIDTH // 8, 3 * HEIGHT // 8),
    "tr32": (6 * WIDTH // 8, 3 * HEIGHT // 8),
    "tr31": (7 * WIDTH // 8, 3 * HEIGHT // 8),
    "tr3": (WIDTH, 3 * HEIGHT // 8),

    "cl": (0, 4 * HEIGHT // 8),
    "cl1": (WIDTH // 8, 4 * HEIGHT // 8),
    "cl2": (2 * WIDTH // 8, 4 * HEIGHT // 8),
    "cl3": (3 * WIDTH // 8, 4 * HEIGHT // 8),
    "c": (4 * WIDTH // 8, 4 * HEIGHT // 8),  # Center
    "cr3": (5 * WIDTH // 8, 4 * HEIGHT // 8),
    "cr2": (6 * WIDTH // 8, 4 * HEIGHT // 8),
    "cr1": (7 * WIDTH // 8, 4 * HEIGHT // 8),
    "cr": (WIDTH, 4 * HEIGHT // 8),

    "bl3": (0, 5 * HEIGHT // 8),
    "bl31": (WIDTH // 8, 5 * HEIGHT // 8),
    "bl32": (2 * WIDTH // 8, 5 * HEIGHT // 8),
    "bl33": (3 * WIDTH // 8, 5 * HEIGHT // 8),
    "bc3": (4 * WIDTH // 8, 5 * HEIGHT // 8),
    "br33": (5 * WIDTH // 8, 5 * HEIGHT // 8),
    "br32": (6 * WIDTH // 8, 5 * HEIGHT // 8),
    "br31": (7 * WIDTH // 8, 5 * HEIGHT // 8),
    "br3": (WIDTH, 5 * HEIGHT // 8),

    "bl2": (0, 6 * HEIGHT // 8),
    "bl21": (WIDTH // 8, 6 * HEIGHT // 8),
    "bl22": (2 * WIDTH // 8, 6 * HEIGHT // 8),
    "bl23": (3 * WIDTH // 8, 6 * HEIGHT // 8),
    "bc2": (4 * WIDTH // 8, 6 * HEIGHT // 8),
    "br23": (5 * WIDTH // 8, 6 * HEIGHT // 8),
    "br22": (6 * WIDTH // 8, 6 * HEIGHT // 8),
    "br21": (7 * WIDTH // 8, 6 * HEIGHT // 8),
    "br2": (WIDTH, 6 * HEIGHT // 8),

    "bl1": (0, 7 * HEIGHT // 8),
    "bl11": (WIDTH // 8, 7 * HEIGHT // 8),
    "bl12": (2 * WIDTH // 8, 7 * HEIGHT // 8),
    "bl13": (3 * WIDTH // 8, 7 * HEIGHT // 8),
    "bc1": (4 * WIDTH // 8, 7 * HEIGHT // 8),
    "br13": (5 * WIDTH // 8, 7 * HEIGHT // 8),
    "br12": (6 * WIDTH // 8, 7 * HEIGHT // 8),
    "br11": (7 * WIDTH // 8, 7 * HEIGHT // 8),
    "br1": (WIDTH, 7 * HEIGHT // 8),

    "bl": (0, HEIGHT),  # Bottom Left
    "bl01": (WIDTH // 8, HEIGHT),
    "bl02": (2 * WIDTH // 8, HEIGHT),
    "bl03": (3 * WIDTH // 8, HEIGHT),
    "bc": (4 * WIDTH // 8, HEIGHT),
    "br03": (5 * WIDTH // 8, HEIGHT),
    "br02": (6 * WIDTH // 8, HEIGHT),
    "br01": (7 * WIDTH // 8, HEIGHT),
    "br": (WIDTH, HEIGHT),  # Bottom Right
}

WINDOW_WIDTH = 1  # 1
WINDOW_HEIGHT = 1  # 1

BASE_WINDOW_SCALE = 100  # 1920 x 1080
WINDOW_SCALE = 0.5  # 0.5
TRANSPARENCY_UNDER_WINDOW = 75  # 75, 128

# --- Card ---

CARD_WIDTH = 2  # 2
CARD_HEIGHT = 3  # 3

BASE_CARD_SCALE = 110  # 1920 x 1080
CARD_SCALE_COEF = 0.1  # 0.27
CARD_SCALE = BASE_CARD_SCALE * ((RES[0] * RES[1]) / (BASE_RES[0] * BASE_RES[1])) ** CARD_SCALE_COEF  # 1920 x 1080, 110

FRAME_WIDTH = 20  # 20, px  # NEED RENAME!!!

# --- Player ---

BASE_HP = 100  # 100 - стартовое значение Здоровья
HEALTH_COEFFICIENT = 30  # 30 - сколько ХП прибавляется за каждую единицу strength
HEALTH_DECREASE_FACTOR = 0.2  # 0.2 - во сколько будет уменьшаться HEALTH_COEFFICIENT за единицу strength

BASE_SPEED = 10  # 10 - стартовое начение Скорости
SPEED_COEFFICIENT = 10  # 10 - сколько Скорости прибавляется за каждую единицу dexterity
SPEED_DECREASE_FACTOR = 0.8  # 0.8 - во сколько будет уменьшаться SPEED_COEFFICIENT за единицу dexterity

# --- Button ---

BUTTON_WIDTH = 2
BUTTON_HEIGHT = BUTTON_WIDTH / 2

BASE_BUTTON_SCALE = 100  # 1920 x 1080
BUTTON_SCALE_COEF = 0.27  # 0.27
BUTTON_SCALE = BASE_BUTTON_SCALE * ((RES[0] * RES[1]) / (BASE_RES[0] * BASE_RES[1])) ** BUTTON_SCALE_COEF
# 1920 x 1080, 100

# ---

# Игра:
# Включить автопасование
# Задержка перед отображением подсказок

# Видео:
# Полноэкранный режим
# Разрешение

# Аудио:
# Звук: общий, музыка, эффекты


# print(SCREEN_POS)
# print(SCREEN_POS["topleft"])
# print(SCREEN_POS["topcenter"])
# print(SCREEN_POS["topright"])
