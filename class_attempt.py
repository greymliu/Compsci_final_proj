class flower:
    color = ""
    size = ""
    petal_shape =""
    petal_num = 0
    latin_binom =""
    name = ""

    def __init__(self, argcolor, argsize, argpetal_shape, argpetal_num, arglatin_binom, argname):
        self.color = argcolor
        self.size = argsize
        self.shape = argpetal_shape
        self.petal_num = argpetal_num
        self.latin_binom = arglatin_binom
        self.name = argname
flw_list = []
Trillium = flower( "white", "small", "lily family", 3, "Trillium grandiflorum","Trillium")
flw_list.append(Trillium)
Angelica = flower( "white", "waist height", "parsley family", 0, "Angelica atropupurea", "Angelica")
flw_list.append(Angelica)
Black_Eye_Susan = flower("yellow", "knee height", "daisy like", 10, "Rudbeckia hirta", "Black Eye Susan")
flw_list.append(Black_Eye_Susan)
Marsh_Marigold = flower("yellow", "knee height", "buttercup like", 5, "Caltha palustris", "Marsh Marigold")
flw_list.append(Marsh_Marigold)
Tiger_Lily = flower("orange", "waist height", "lily family", 6, "Liliumm tigrinum", "Tiger Lily")
flw_list.append(Tiger_Lily)
Butterfly_Weed = flower("orange", "small", "milkweed family", 0, "Asclepias tuberosa", "Butterfly Weed" )
flw_list.append(Butterfly_Weed)

flw_color = input("What color is your flower? Options: white, yellow, orange: ")

for f in flw_list:
    if flw_color == f.color:
        print("Your flower could be a:\n" + f.name)
flw_size = input("What size is your flower? Options: small, knee height, waist height: ")
for f in flw_list: 
    if flw_color == f.color and flw_size == f.size:
        print("Your flower could be a:\n" + f.name)
    else:
        print("Your flower isn't in the database.\n You can add it by answering the next several questions")
        flw_shape = input("What shape is your flower? Options: lily family, parsley family, daisy like, buttercup like, milkweed family: ")
        flw_num = input("How many petals does your flower have? If N/A put 0: ")
        flw_latin_binom = input("What is your flower's latin binomial? If unkown write xxx: ")
        flw_name = input("What is your flower's name? If unknown put xxx: ")
        unknown_flower = flower(flw_color, flw_size, flw_shape, flw_num, flw_latin_binom, flw_name)
        flw_list.append(unknown_flower)
        for f in flw_list:
            print(f.name, f.color, f.size)
        y_n = input("Do you see your flower?[y/n]")
        if y_n == 'y':
            break


flw_shape = input("What shape is your flower? Options: lily family, parsley family, daisy like, buttercup like, milkweed family: ")
for f in flw_list:
    if flw_color == f.color and flw_size == f.size and flw_shape == f.shape:
        print( "Your flower could be a:\n" + f.name)
    else:
        print("Your flower isn't in the database.\n You can add it by answering the next several questions")
        






# if flw_color == "white":
#     for f in flw_list:
#         if f.color == "white":
#             print("Your flower could be a\n" + f.name)
# if flw_color == "orange":
#     for f in flw_list:
#         if f.color == "orange":
#             print("Your flower could be a\n" + f.name)
# if flw_color == "yellow":
#     for f in flw_list:
#         if f.color == "yellow":
#             print("Your flower could be a\n" + f.name)
# flw_size = input("What size is your flower? Options: small, knee height, waist height: ")
# if flw_color == "white" and flw_size == "small":
#     for f in flw_list:
#         if f.color == "white" and f.size == "small":
#             print("Your flower could be a\n" + f.name)
# if flw_color == "white" and flw_size == "waist height":
#     for f in flw_list:
#         if f.color == "white" and flw_size == "waist height":
#             print("Your flower could be a\n" + f.name)
# if flw_color == "orange" and flw_size == "small":
#     for f in flw_list:
#         if f.color == "orange" and f.size == "small":
#             print("Your flower could be a\n" + f.name)
# if flw_color == "orange" and flw_size == "waist height":
#     for f in flw_list:
#         if f.color == "orange" and f.size == "waist height":
#             print("Your flower could be a\n" + f.name)
# if flw_color == "yellow":
#     for f in flw_list:
#         if f.color == "yellow":
#             print("Your flower could be a\n" +f.name)
# if flw_color == "yellow" and flw_size == "knee height":
#     for f in flw_list:
#         if f.color == flw_color and f.size == flw_size:
#             print("Your flower could be a\n" + f.name)
#             flw_shape = input("What shape is your flower? Options: lily family, parsley family, daisy like, buttercup like, milkweed family: ")
#             if flw_shape == "daisy like":
#                 if f.shape =="daisy like":
#                     print("Your flower could be a\n" + f.name)
#             elif f.shape == "buttercup like":
#                 if f.shape == "buttercup like":
#                     print("Your flower could be a\n" + f.name)
# else:
#     print("Your flower is not in the database")


