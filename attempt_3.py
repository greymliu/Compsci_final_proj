class Trillium:
    name = "Trillium"
    color = "white"
    size = "ground cover"
    properties = "xxx"
    petal_shape = "rounded"
    latin_binom = "xxx"
    petal_num = 3
    additional_info = "xxxx"
class LadySlipper:
    name = "Lady Slipper"
    color = "white"
    size = "knee height"
    petal_shape = "cup-like"
class BloodRoot:
    name = "Blood Root"
    color = "white"
    size = "ground cover"
    petal_num = 8
class RueAnemone:
    name = "Rue Anemone"
    color = "white"
    size = "ground cover"
    properties = "xxx"
    petal_num = 5
class Yarrow:
    name = "Yarrow"
    color = "white"
    size = "knee height"
class SolomonsSeal:
    name = "Solomon's Seal"
    color = "yellow"
    size = "small"
class CommonMullien:
    name = "Common Mullien"
    color = "yellow"
    size = "waist height to tall"
class CommonStJohnsWort:
    name = "Common St Johns Wort"
    color = "yellow"
    size = "knee height"


flw_colors = ["white", "yellow","orange", "blue/violet", "red/pink"]
flw_sizes = ["ground cover", "small", "knee height", "waist height to tall"]



while True:
    flw_color = input(f"What color is you're flower? Options: {flw_colors}")
    if flw_color == "white":
        if flw_size == "ground cover":
            flw_petal_num = input(f"How many petals does you're flower have?")
            if flw_petal_num == "8":
                print("You're flower is Blood Root")
                break
            if flw_petal_num == "5":
                print("You're flower is a Rue Anenome")
                break
            if flw_petal_num =="3":
                print("You're flower is a Trillium")
                break
        flw_size = input(f"What size is you're flower? Options: {flw_sizes}")
        if flw_size == "small":
            print("We don't have a large enough database to find this flower")
            break
        if flw_size == "knee height":
            print("You're flower is a Lady Slipper")
            break






