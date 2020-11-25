# Цвета
CYAN = (0, 240, 240)
BLUE = (0, 0, 240)
MUSTARD = (240, 160, 0)
YELLOW = (240, 240, 0)
GREEN = (0, 240, 0)
VIOLET = (160, 0, 240)
RED = (240, 0, 0)
colors = [CYAN, BLUE, MUSTARD, YELLOW,
          GREEN, VIOLET, RED
          ]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Настроечные константы
FPS = 30
width = 900  # ширина экрана
height = 800  # высота экрана
cube_edge = 35  # ребро одного кубика
glass_x = 200  # экранная координата x левого верхнего угла "стакана"
glass_y = 50  # экранная координата y левого верхнего угла "стакана"
next_box_x = 600  # экранная координата x левого верхнего угла поля со следующей фигурой
next_box_y = 50  # экранная координата y левого верхнего угла поля со следующей фигурой


# Словарь фигур
# Порядок следования кубиков в словаре: самый нижний, самый левый, самый правый, оставшийся
# Порядок следования строк в списке списков: от нормальной ориентации по часовой стрелке
figure_dict = {'I': [[(0, 2), (0, 1), (0, 0), (0, -1)],
                     [(0, 0), (-1, 0), (2, 0), (1, 0)],
                     [(0, 2), (0, 1), (0, 0), (0, -1)],
                     [(0, 0), (-1, 0), (2, 0), (1, 0)]],

               'J': [[(0, 1), (-1, 1), (0, 0), (0, -1)],
                     [(0, 0), (-1, 0), (1, 0), (-1, -1)],
                     [(0, 1), (0, 0), (1, -1), (0, -1)],
                     [(1, 1), (-1, 0), (1, 0), (0, 0)]],

               'L': [[(0, 1), (0, 0), (1, 1), (0, -1)],
                     [(-1, 1), (-1, 0), (1, 0), (0, 0)],
                     [(0, 1), (-1, -1), (0, 0), (0, -1)],
                     [(0, 0), (-1, 0), (1, 0), (1, -1)]],

               'O': [[(0, 0), (0, -1), (1, 0), (1, -1)],
                     [(0, 0), (0, -1), (1, 0), (1, -1)],
                     [(0, 0), (0, -1), (1, 0), (1, -1)],
                     [(0, 0), (0, -1), (1, 0), (1, -1)]],

               'S': [[(1, 1), (0, 0), (1, 0), (0, -1)],
                     [(0, 0), (-1, 0), (1, -1), (0, -1)],
                     [(1, 1), (0, 0), (1, 0), (0, -1)],
                     [(0, 0), (-1, 0), (1, -1), (0, -1)]],

               'T': [[(0, 1), (0, 0), (1, 0), (0, -1)],
                     [(0, 1), (-1, 0), (1, 0), (0, 0)],
                     [(0, 1), (-1, 0), (0, 0), (0, -1)],
                     [(0, 0), (-1, 0), (1, 0), (0, -1)]],

               'Z': [[(0, 1), (0, 0), (1, 0), (1, -1)],
                     [(0, 0), (-1, -1), (1, 0), (0, -1)],
                     [(0, 1), (0, 0), (1, 0), (1, -1)],
                     [(0, 0), (-1, -1), (1, 0), (0, -1)]]
               }
