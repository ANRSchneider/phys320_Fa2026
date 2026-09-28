
list_of_files = [ "Food.csv", 
                 "Hyvee_9_21_Ana.csv",
                 "Jackson_food_items.txt",
                 "Lanes_Shopping_List.csv",
                 "Mareks_food_items.txt",
                 "Nates_Foods_from_Fareway.csv",
                 "Nathans_food_items.txt"]

for filename in list_of_files:
    print(filename)

    f=open(filename, 'r')
    print (f.readline())


