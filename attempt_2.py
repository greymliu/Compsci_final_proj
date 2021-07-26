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
    properties = "xxx"
class Yarrow:
    color = "white"
    size = "knee height"
class SolomonsSeal:
    color = "yellow"
    size = "small"
class CommonMullien:
    color = "yellow"
    size = "waist height to tall"
class CommonStJohnsWort:
    color = "yellow"
    size = "knee height"

flowers = [Trillium, Yarrow]

white_flws = [Trillium, BloodRoot, LadySlipper,RueAnemone, Yarrow]
white_gc_flws = [Trillium, RueAnemone, BloodRoot]

yellow_flws = [SolomonsSeal, CommonMullien, CommonStJohnsWort]

flw_colors = ["white", "yellow","orange", "blue/violet", "red/pink"]
flw_sizes = ["ground cover", "small", "knee height", "waist height to tall"]
flw_color = input(f"What color is you're flower? Options: {flw_colors}")
flw_size = input(f"What size is you're flower? Options: {flw_sizes}")
flw_petal_num = input(f"How many petals does you're flower have?")
flw = []


while True:
    if flw_color == "white":
        flw.extend(white_flws)
        if flw_size == "ground cover":
            flw.extend(white_gc_flws)
            if flw_petal_num == "3" :
                print("You're flower is a trillium!")
                print(Trillium.properties)
            if flw_petal_num == "5":
                print("You're flower is a Rue Anenome!")
                print(RueAnemone.properties)
            if flw_petal_num == "8":
                print("You're flower is Blood Root!")

        if flw_size == "knee height":
            flw.extend(Yarrow)
            print("You're flower is Yarrow")

        break
    if flw_color == "yellow":
        flw.extend(yellow_flws)
    if flw_size == "small":
        flw.append(SolomonsSeal)
        break


