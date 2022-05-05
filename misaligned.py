def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            checkValidPairNumber(i*5+j+1)
            print(f'{i * 5 + j : <2} | {major:<6} | {minor:<6}')
    return len(major_colors) * len(minor_colors)
def checkValidPairNumber(pair_number):
    assert(pair_number>0)
    assert(pair_number<=25)

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
