def main():
    add_x_to_y(9, 11)
    add_x_to_y(0, 10)
    add_x_to_y(5, 2)
    add_x_to_y(-2, 5)


def add_x_to_y(x, y):
    """Add numbers from x to y"""
    if y < x:
        print("0")
    else:
        # total = 0
        # for i in range(x, y):
        #     total += i
        # total += y
        # print(total)
        total = sum(range(x, y + 1))
        print(total)

main()

