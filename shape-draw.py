# The draw_square functon will draw a square based on the size of the square side
def draw_square(side):
    # two nested for loops to draw each line of the square
    for i in range(side):
        for j in range(side):
            print('*  ', end='')
        print()  # Move to the next line


# The draw_rectangle function will draw a rectangle based on the sizes of the long and short sides
def draw_rectangle(long_side, short_side):
    # two nested for loops to draw each line of the long side based on the height of the short side
    for i in range(short_side):
        for j in range(long_side):
            print('*  ', end='')
        print()  # Move to the next line


# The triangle function will draw an equidistant triangle based on the
# size of the base and the height of the triangle
def draw_triangle(base, height):
    # Calculate the step size for the number of asterisks in each row
    step = (base - 1) / (height - 1)

    # Draw the triangle
    for i in range(height):
        # Calculate the number of asterisks for the current row
        num_stars = 1 + round(i * step)

        # Ensure the last row has exactly 'base' asterisks
        if i == height - 1:
            num_stars = base

        # Calculate the padding on each side
        padding = (base - num_stars) // 2

        # Print the row
        print(' ' * padding + '*' * num_stars)


# The main loop will interactively ask for the shape to draw and request additional
# input based on the first selection
while True:
    print("Pick shape to draw")
    shape = int(input("1 for square, 2 for rectangle, 3 for triangle, any other key to quit\n"))

    # depending on shape, call the respective function with the proper parameters
    match shape:
        case 1:
            square_side = int(input('Enter square side size: '))
            draw_square(square_side)
        case 2:
            rectangle_long_side = int(input('Enter rectangle long side: '))
            rectangle_short_side = int(input('Enter rectangle short side: '))
            draw_rectangle(rectangle_long_side,rectangle_short_side)
        case 3:
            triangle_base = int(input('Enter triangle base (must be odd number for perfect shaping): '))
            triangle_height = int(input('Enter triangle height: '))
            # adjust base to odd number if user entered an even number
            if triangle_base % 2 == 0:
                triangle_base += 1
            draw_triangle(triangle_base, triangle_height)
        case _:
            print('Invalid Entry')
            break
