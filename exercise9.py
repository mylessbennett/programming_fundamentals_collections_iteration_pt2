grocery_list = ["bread", "apples", "milk", 'salmon', 'bananas']
#---------------------------------------------------------------
for food in grocery_list:
    print("* {}".format(food))
#---------------------------------------------------------------
grocery_list.append("rice")
#---------------------------------------------------------------
def print_grocery_list(grocery_list):
    for food in grocery_list:
        print("* {}".format(food))
    return
#---------------------------------------------------------------
print_grocery_list(grocery_list)
#---------------------------------------------------------------
print(len(grocery_list))
#---------------------------------------------------------------
def check_for_bananas(grocery_list):
    bananas = False
    for food in grocery_list:
        if food == "bananas":
            bananas = True

    if bananas == True:
        print("You don't need to pick up bananas today")
    else:
        print("You need to pick up bananas!")
    return

check_for_bananas(grocery_list)
#---------------------------------------------------------------
print(grocery_list[1])
#---------------------------------------------------------------
new_list = sorted(grocery_list)
print_grocery_list(new_list)
new_list.remove('salmon')
print(new_list)
