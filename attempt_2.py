from PIL import Image
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

flowers = [Trillium, LadySlipper, BloodRoot, RueAnemone, Yarrow, SolomonsSeal, CommonStJohnsWort, CommonMullien]

flw_colors = ["white", "yellow","orange", "blue/violet", "red/pink"]
flw_sizes = ["ground cover", "small", "knee height", "waist height to tall"]
flw_color = input(f"What color is you're flower? Options: {flw_colors}")
flw_size = input(f"What size is you're flower? Options: {flw_sizes}")

while True:
    if flw_color == "white":
        if flw_size == "ground cover":
            flw_petal_num = input(f"How many petals does you're flower have?")
            if flw_petal_num == "3" :
                print("You're flower is a trillium!")
                print(Trillium.properties)
                break
            if flw_petal_num == "5":
                print("You're flower is a Rue Anenome!")
                print(RueAnemone.properties)
                break
            if flw_petal_num == "8":
                print("You're flower is Blood Root!")
                break
        if flw_size == "knee height":
            print("You're flower is Yarrow")
            break
    if flw_color == "yellow":
        if flw_size == "small":
            leaf_shape = input("What are the leaves of you're flower? (options: heart shaped, flat, jagged with three parts) ")
        if leaf_shape == "heart shaped":
                    print("You're flower is a Marsh Marigold")
        if leaf_shape == "jagged with three parts":
                    print("You're flower is a Swamp Buttercup")
        if leaf_shape == "flat":
            q = input("Does you're flower have 5 petals? [y/n]")
            if q == "y":
                print("You're flower is Clintonia")
            else:
                print("You're flower is Solomon's Seal")


