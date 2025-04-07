# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Настройки сетки
GRID_SIZE = 8
TILE_SIZE = 50
GRID_OFFSET_X = 50
GRID_OFFSET_Y = 100

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]

# Настройки монстров
BASE_MONSTER_HP = 20
BASE_MONSTER_DAMAGE = 5
BASE_MONSTER_SPEED = 0.5
SPAWN_INTERVAL = 3000  # 3 секунды
MONSTER_PATH_Y = 50  # Высота дорожки монстров
GRID_OFFSET_Y = MONSTER_PATH_Y + 70  # Смещаем игровое поле ниже

# Настройки крепости
CASTLE_HP = 100
CASTLE_WIDTH = 60
CASTLE_HEIGHT = 100

# Меню
MENU_BG_COLOR = (50, 50, 80)
BUTTON_COLOR = (70, 70, 120)
BUTTON_HOVER_COLOR = (90, 90, 140)
TEXT_COLOR = (255, 255, 255)

# Добавляем настройки сложности
DIFFICULTY_SETTINGS = {
    "новичок": {
        "monster_hp": 15,
        "monster_damage": 3,
        "monster_speed": 0.3,
        "spawn_interval": 4000,
        "castle_hp": 100
    },
    "любитель": {
        "monster_hp": 25,
        "monster_damage": 5,
        "monster_speed": 0.5,
        "spawn_interval": 3000,
        "castle_hp": 100
    },
    "профи": {
        "monster_hp": 40,
        "monster_damage": 8,
        "monster_speed": 0.7,
        "spawn_interval": 2000,
        "castle_hp": 100
    }
}

WIN_SCORE = 100  # Количество очков для победы
