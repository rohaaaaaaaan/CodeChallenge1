def draw_grid(rows, cols):
    # Drawing the top border of the grid
    top_border = "+ " + " - " * 4 + " + " + " - " * 4 + " +"
    print(top_border)

    # Each cell in the grid
    for row in range(rows):
        for r in range(4):  # Drawing 4 rows of cells
            line = "| " + " " * 10 + " | " + " " * 12 + " |"
            print(line)
        
        # Bottom border of the current grid section
        print(top_border)

# Customizable grid dimensions
draw_grid(2, 2)  # Adjust the numbers for more or less rows/columns
