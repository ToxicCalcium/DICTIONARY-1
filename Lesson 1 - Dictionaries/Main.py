l1 = [1, 7, 3, 5000000, 89898987]
#Creating a Dictionary
sample_dict = {
    "sample_key" : "sample_value",
    "name" : "Raghav",
    "age" : 13,
    "editor" : "vscode",
    "device" : "pc"
}

#printing a whole dictionary
print(sample_dict)

#printing a specific portion of a dictionary
print(sample_dict["device"])
print(sample_dict["sample_key"])

#getting a list of all the Dictionary keys
print(sample_dict.keys())

#getting a list of all the Dictionary values
print(sample_dict.values())

#applying FOR loops in a dictionary
for key in sample_dict.keys():
    print(key, ":", sample_dict[key])

#checking if a key exists in a dictionary
if "sample_key" in sample_dict:
    print("key exists")
else:
    print("key does not exist")

if "fake_sample_key" in sample_dict:
    print("key exists")
else:
    print("key does not exist")

#adding key & value pairs during run time
sample_dict["new_sample_key"] = "new_sample_value"
sample_dict["profession"] = "game_developer"
print(sample_dict)

#deleting a key & value pair
del(sample_dict["new_sample_key"])
print (sample_dict)

#changing the value of a key in a dictionary
sample_dict["profession"] = "banker"
print(sample_dict)

#storing a list as a value in a dictionary
sample_dict["marks"] = [56, 33, 1, 100, 99, 98]
print(sample_dict)

#accessing a value in the list within a dictionary
print(sample_dict["marks"][3])