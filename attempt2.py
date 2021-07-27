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

while True:
    if flw_color == "white":
        flw_size = input(f"What size is you're flower? Options: {flw_sizes}")
        if flw_size == "ground cover":
            flw_petal_num = input(f"How many petals does you're flower have?")
            if flw_petal_num == "3" :
                print("Your flower is a trillium!")
                print(Trillium.properties)
                break
            if flw_petal_num == "5":
                print("Your flower is a Rue Anenome!")
                print(RueAnemone.properties)
                break
            if flw_petal_num == "8":
                print("Your flower is Blood Root!")
                break
        if flw_size == "knee height":
            print("Your flower is Yarrow")
            break
    if flw_color == "yellow":
        flw_size = input("What size is your flower? Options: (small, knee height, waist height to tall)")
        if flw_size == "small":
            leaf_shape = input("What are the leaves of you're flower? (options: heart shaped, flat, jagged with three parts) ")
        if leaf_shape == "heart shaped":
                    print("Your flower is a Marsh Marigold")
                    break
        if leaf_shape == "jagged with three parts":
                    print("Your flower is a Swamp Buttercup")
                    break
        if leaf_shape == "flat":
            q = input("Does you're flower have 5 petals? [y/n]")
            if q == "y":
                print("You're flower is Clintonia")
                break
            else:
                print("You're flower is Solomon's Seal")
                break
        if flw_size == "knee height":
            leaf_shape = input('What is the leaf shape of your flower? Options:(small leaflets coming directly off the stem, long serrated leaflets)')
            if leaf_shape == 'small leaflets coming directly off the stem':
                print("You're flower is a Common St. John's Wort")
                break
            else:
                print("Your flower is a Tansy")
                break
        if flw_size == "waist height to tall":
            print("Your flower is a Common Mullien")
            break
    if flw_color == "orange":
        flw_size = input("What size is your flower? Options: (vine, small, tall)")
        if flw_size == "vine":
            print("Your flower is Trumpet Honeysuckle")
            break
        if flw_size == "small":
            print("Your flower is Butterflyweed")
            break
        if flw_size == "tall":
            print( "Your flower is a Tiger Lily")

    




