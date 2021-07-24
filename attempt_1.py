flw_colors = ["yellow", "blue"]
yellow_flowers = ["yellow iris", "touch me not", "trout-lily"]

possible_flw = []
color_q = input(f'What color is your flower (options {flw_colors})?')

while True:
    if color_q == "yellow":
        possible_flw.append(yellow_flowers)
        print(f"You're flower may be a {possible_flw}")
        break

    else:
        print(possible_flw)
        break


