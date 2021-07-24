class Trillium:
    color = "white"
    size = "ground cover"
    properties = "xxx"
    petal_shape = "rounded"
    latin_binom = "xxx"
    petal_num = 3
    additional_info = "xxxx"
class LadySlipper:
    color = "white"
    size = "knee height"
    petal_shape = "cup-like"
class BloodRoot:
    color = "white"
    size = "ground cover"
class RueAnemone:
    color = "white"
    size = "ground cover"
class Yarrow:
    color = "white"
    size = "knee height"
class SolomonsSeal:
    color = "yellow"
    size = "small"
class CommonMullien:
    color = "yellow"
    size = "waist height to tall"

flw_colors = ["white", "yellow","orange", "blue/violet", "red/pink"]
flw_sizes = ["ground cover", "small", "knee height", "waist height to tall"]
flw_color = input(f"What color is you're flower? Options: {flw_colors}")
flw_size = input(f"What size is you're flower? Options: {flw_sizes}")
flw_petal_num = input(f"How many petals does you're flower have?")
flw = []
while True:
    if flw_color == "white":
        flw.append(Trillium, LadySlipper, BloodRoot, RueAnemone, Yarrow)
        if flw_size == "ground cover":
            flw.append(Trillium, RueAnemone, BloodRoot)
            if flw_petal_num = 3:
                print("You're flower is a trillium!")
                print(Trillium.properties)
        break
    if flw_color == "yellow":
        flw.append(SolomonsSeal, CommonMullien)
    
        break


