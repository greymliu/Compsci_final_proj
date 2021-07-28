
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
                break
            if flw_petal_num == "5":
                print("Your flower is a Rue Anenome!")
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
            ##Add pics for leaf shapes!!!
            if leaf_shape == 'small leaflets coming directly off the stem':
                print("You're flower is a Common St. John's Wort")
                break
            if leaf_shape == "long serrated leflets":
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
    if flw_color == "blue" or "violet" or "blue/violet":
        flw_size = input("What size is your flower? Options: (small, knee height, waist height)")
        if flw_size == "small":
            print("Your flower is Corn Flower")
            break
        if flw_size == "knee height":
            y_n = input("Do petals come off your flower's center?[y/n]")
            if y_n == 'y':
                print("Your flower is Echinacea")
                break
            else:
                q_4 = input("Does")
                #USE IMAGES DO DIFFER BETWEEN LOBELIA AND LUPINE
                break
        if flw_size == "knee height":
            flw_shape = input("what shape is your flower? Options: (small off of a spike, large with three petals going outwards)")
            if flw_shape == "small off of a spike":
                print("Your flower is Blue Vervain")
                break
            else:
                print("Your flower is an Iris")
                break



    




