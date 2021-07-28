print("""Welcome to find-your-flower!! After answering 
a few questions you should be able to know what species your flower is.\n 
A Note: flower shapes are defined as...""")
# (lily family, parsley family,
# daisy like, buttercup like, milkweed family, rose family, crowded spike,
# blue bell and pea family)
##Add pictures about what flower shape means

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
Pasture_Rose = flower("pink", "small", "rose family", 5,"Rosa carolina", "Pasture Rose")
flw_list.append(Pasture_Rose)
Blazing_Star = flower("pink", "knee height", "crowded spikes", 0, "Liatris pycnostachya", "Blazing Star")
flw_list.append(Blazing_Star)
Lupine = flower("violet", "knee height", "pea family",2, "Lupinus prennis", "Lupine")
flw_list.append(Lupine)
Lobelia = flower("violet", "knee height", "blue bell family", 5, "Lobelia siphilitica", "Lobelia")
flw_list.append(Lobelia)

flw_shape_list = ["lily family", "parsley family", 
"daisy like","buttercup like", "milkweed family", 
"blue bell family", "crowded spikes","rose family",
"pea family"]
possible_flw =[]
flw_color = input("What color is your flower? Options: white, yellow, orange, pink, violet: ")
for f in flw_list:
    if flw_color == f.color:
        print("Your flower could be a:\n" + f.name)

flw_size = input("What size is your flower? Options: small, knee height, waist height: ")
for f in flw_list: 
    if flw_color == f.color and flw_size == f.size:
        possible_flw.append(f.name)
        print("Your flower could be a:\n" + f.name)
        if len(possible_flw) == 1:
            exit()

flw_shape = input(f"What shape is your flower? Options: {flw_shape_list}")
for f in flw_list:
    if flw_color == f.color and flw_size == f.size and flw_shape == f.shape:
        possible_flw.append(f.name)
        print("Your flower could be a:\n" + f.name)
        if len(possible_flw) == 1:
            exit()



        






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


