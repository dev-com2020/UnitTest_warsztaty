from unittest.mock import Mock, patch

PI = 3.14159

def rectangle(sideA, sideB):
    return sideA * sideB

def circle(radius):
    return 2 * PI * radius


def calculate_area(shape, sizeA, sizeB=0):
    if sizeA <= 0:
        raise ValueError('Wartość sizeA musi być dodatnia')
    if sizeB < 0:
        raise ValueError('Wartość sizeB musi być dodatnia')
    if shape == 'SQUARE':
        return rectangle(sizeA, sizeA)
    if shape == 'RECTANGLE':
        return rectangle(sizeA, sizeB)
    if shape == 'CIRCLE':
        return circle(sizeA)
    raise Exception(f'Figura {shape} nie jest zdefiniowana')


# mock = Mock()
# mock.side_effect = (1, 2, 3)
# # print(mock())
# # print(mock())
# # print(mock())
# with patch('dependencies.PI',2):
#     print(circle(2))