import tkinter
from PIL import Image
print("""Welcome to find-your-flower!! After answering 
a few questions you should be able to know what species your flower is.\n 
A Note: you can find more info about flower shapes by answering the questions below""")
lilyfam = input("Do you want to know more about lily family? [y/n]")
parsleyfam = input("Do you want to know more about parsley family? [y/n]")
daisyfam = input("Do you want to know more about daisy family? [y/n]")
buttercupfam = input("Do you want to know more about buttercup family? [y/n]")
milkweedfam = input("Do you want to know more about milkweed family? [y/n]")
rosefam = input("Do you want to know more about rose family? [y/n]")
crowdedspike = input("Do you want to know more about crowded spike family? [y/n]")
bluebellfam = input("Do you want to know more about blue bell family? [y/n]")
peafam = input("Do you want to know more about pea family? [y/n]")
im_lily = Image.open("flower_folder2/lily_ex.jpg")
im_parsley = Image.open("flower_folder2/parsley_ex.jpg")
im_daisy = Image.open("flower_folder2/daisy_ex.jpg")
im_buttercup2 = Image.open("flower_folder2/buttercup_descrip.jpg")
im_milkweed2 = Image.open("flower_folder2/milkweed_descrip.jpg")
im_rose = Image.open("flower_folder2/rose_ex.jpg")
im_rose2 = Image.open("flower_folder2/rose_descrip.jpg")
im_crowdedspike = Image.open("flower_folder2/crowded_spike_ex.jpg")
im_bluebell = Image.open("flower_folder2/bluebell_ex.jpg")
im_bluebell2 = Image.open("flower_folder2/bluebell_descrip.jpg")
im_pea = Image.open("flower_folder2/pea_descrip.jpg")
if lilyfam == "y":
    im_lily.show()
if parsleyfam == 'y':
    im_parsley.show()
if daisyfam == 'y':
    im_daisy.show()
if buttercupfam == 'y':
    im_buttercup2.show()
if milkweedfam == 'y':
    im_milkweed2.show()
if rosefam == 'y':
    im_rose.show()
    im_rose2.show()
if crowdedspike == 'y':
    im_crowdedspike.show()
if bluebellfam == 'y':
    im_bluebell.show()
    im_bluebell2.show()
if peafam == 'y':
    im_pea.show()

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
Trillium = flower( "white", "small", "lily family", "3", "Trillium grandiflorum","Trillium")
flw_list.append(Trillium)
Angelica = flower( "white", "waist height", "parsley family", "0", "Angelica atropupurea", "Angelica")
flw_list.append(Angelica)
Black_Eye_Susan = flower("yellow", "knee height", "daisy like", "10", "Rudbeckia hirta", "Black Eye Susan")
flw_list.append(Black_Eye_Susan)
Marsh_Marigold = flower("yellow", "small", "buttercup like", "5", "Caltha palustris", "Marsh Marigold")
flw_list.append(Marsh_Marigold)
Tiger_Lily = flower("orange", "waist height", "lily family", "6", "Liliumm tigrinum", "Tiger Lily")
flw_list.append(Tiger_Lily)
Butterfly_Weed = flower("orange", "small", "milkweed family", "0", "Asclepias tuberosa", "Butterfly Weed" )
flw_list.append(Butterfly_Weed)
Pasture_Rose = flower("pink", "small", "rose family", "5","Rosa carolina", "Pasture Rose")
flw_list.append(Pasture_Rose)
Blazing_Star = flower("pink", "knee height", "crowded spikes", "0", "Liatris pycnostachya", "Blazing Star")
flw_list.append(Blazing_Star)
Lupine = flower("violet", "knee height", "pea family","2","Lupinus prennis", "Lupine")
flw_list.append(Lupine)
Lobelia = flower("violet", "knee height", "blue bell family", "5", "Lobelia siphilitica", "Lobelia")
flw_list.append(Lobelia)
Argrimony = flower("yellow", "knee height", "rose family", "5", "Agrimonia", "Agrimony")
flw_list.append(Argrimony)
Bee_Balm = flower("violet", "waist height", "tubed flower", "0", "Monarda media", "Bee Balm")
flw_list.append(Bee_Balm)
Beardstoungue = flower("violet", "waist height", "tubed flower", "5", "Penstemon grandiflorus", "Beardstoungue")
flw_list.append(Beardstoungue)

flw_shape_list = ["lily family", "parsley family", 
"daisy like","buttercup like", "milkweed family", 
"blue bell family", "crowded spikes","rose family",
"pea family", "tubed flower"]
possible_flw =[]

flw_color = input("What color is your flower? Options: white, yellow, orange, pink, violet: ")
for f in flw_list:
    if flw_color == f.color:
        print("Your flower could be a:\n" + f.name)

flw_size = input("What size is your flower? Options: small, knee height, waist height: ")
for f in flw_list: 
    if flw_color == f.color and flw_size == f.size:
        possible_flw.append(f)
        print("Your flower could be a:\n" + f.name)
    if len(possible_flw) == 1:
        y_n = input("Do you want your flower's latin binomial?[y/n]")
        print(possible_flw)
        if y_n == "y":
            print(possible_flw[0].latin_binom)
        else:
            exit()

flw_shape = input(f"What shape is your flower? Options: {flw_shape_list}")
for f in flw_list:
    if flw_color == f.color and flw_size == f.size and flw_shape == f.shape:
        possible_flw.append(f)
        print("Your flower could be a:\n" + f.name)
    if len(possible_flw) == 1:
        y_n = input("Do you want your flower's latin binomial?[y/n]")
        if y_n == "y":
            print(possible_flw[0].latin_binom)
        else:
            exit()

flw_num = input("How many petals does your flower have?")
for f in flw_list:
    if flw_color == f.color and flw_size == f.size and flw_shape == f.shape and flw_num == f.petal_num:
        possible_flw.append(f)
        print("Your flower could be a: \n" + f.name)
    if len(possible_flw) == 1:
        y_n = input("Do you want your flower's latin binomial?[y/n]")
        if y_n == "y":
            print(possible_flw[0].latin_binom)
        else:
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


