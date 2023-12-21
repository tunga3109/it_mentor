from math import pi

def square_perimeter(length: float): 
    
    return length * 4

def square_quadrate(length: float):
    
    return length ** 2

def square_perimmeter_rectangle(length: float, width: float):
    
    if length == width:
        perimeter = square_perimeter(length)
        square = square_quadrate(length)
        
        return perimeter, square
    
    else:
        perimeter = 2 * (length + width)
        square = length * width
        
        return perimeter, square
    
def circle_length(diameter: float):
    
    return pi * diameter

def cube_volume_square(edge_length: float):
    
    volume = edge_length ** 3
    square = 6 * edge_length ** 2
    
    return volume, square

def cube_volume_rectangular_parallelepiped(edge_length_1: float, edge_length_2: float,edge_length_3: float,):
    
    volume = edge_length_1 * edge_length_2 * edge_length_3
    square = 2 * ((edge_length_1 * edge_length_2) + (edge_length_2 * edge_length_3) + (edge_length_1 * edge_length_3))
    
    return volume, square

def length_square_circle(radius: float):
    
    length = 2 * pi * radius
    square = pi * radius ** 2
    
    return length, square
    
def arithmetical_mean(first_num: float, second_num: float):
    
    return (first_num + second_num)/2

def geometric_mean(first_num: float, second_num: float):
    
    return (first_num * second_num) ** 0.5


def calculate_operations(first_num, second_num):

    sum_of_squares = first_num**2 + second_num**2
    
    difference_of_squares = first_num**2 - second_num**2
    
    product_of_squares = (first_num * second_num)**2
    
    quotient_of_squares = first_num**2 / second_num**2
    
    return sum_of_squares, difference_of_squares, product_of_squares, quotient_of_squares
    
    