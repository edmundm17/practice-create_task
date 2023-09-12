restaurant = "McDonalds","Chick Fil A","Taco Bell","WingStop"

new_res = input("What restaurant would you like to rank into your list")

def rank_restaurant(new_res, restaurant):

    for i in range(len(restaurant)):

        rank = input("Do you like A" + new_res + "more or B" + restaurant[i] + "more? A/B")

        if rank == "A":
            restaurant.insert(i, new_res)
            break
        elif rank == "B":
            continue

    return restaurant

print ("Your new ranking of restaurants is", rank_restaurant(new_res,restaurant))