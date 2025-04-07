def swap_tiles(grid, pos1, pos2):
    """Обмен тайлов местами в сетке"""
    x1, y1 = pos1
    x2, y2 = pos2
    grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]

    # Обновляем координаты в тайлах
    grid[x1][y1].x = x1
    grid[x1][y1].y = y1
    grid[x2][y2].x = x2
    grid[x2][y2].y = y2

    # Обновляем прямоугольники для отрисовки
    grid[x1][y1].update_rect()
    grid[x2][y2].update_rect()
