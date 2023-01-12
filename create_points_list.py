import itertools


def create_points_list():
    # wyznaczenie granicy x i y dla figur / lon i lat
    x_min = 18.59
    x_max = 18.6675
    y_min = 54.34475
    y_max = 54.392

    # tworzenie siatki o szerokości 0.0005
    x_points = [x_min + i * 0.0005 for i in range(int((x_max - x_min) / 0.0005) + 1)]
    y_points = [y_min + i * 0.0005 for i in range(int((y_max - y_min) / 0.0005) + 1)]

    # tworzenie listy wszystkich możliwych punktów
    grid_points = list(itertools.product(x_points, y_points))

    # wyświetlenie listy wszystkich punktów
    print(grid_points)

