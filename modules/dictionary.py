def dictionary_module():
    # empty dict
    # my_dict = {}

    # sample dict with some data
    super_dict = {
        "saba": "She is mine!",
        "2": "Nobody can get her except me!"
    }


    # Accessing values:
    print(super_dict["saba"])
    print(super_dict["2"])


    # Adding and removing keys
    super_dict["ibrahim"] = "Saba Ibrahim!"

    print(super_dict["ibrahim"])

    #  Removing keys
    # del super_dict["ibrahim"]
    # super_dict.pop('ibrahim')

    print(super_dict)

    if "saba" in super_dict:
        print("saba is in the dictionary")
        print(super_dict["saba"])
        
    else:
        print("saba is not in the dictionary")
        
        
    print(super_dict.keys())
    print(super_dict.values())
    print(super_dict.items())

    new_dict = super_dict.copy()
    super_dict.clear();

    print(new_dict)
    print(super_dict)

    dict_1 =  {"a": 1, "b": 2, "c": 3}
    dict_2 = {"d": 4, "e": 5, "f": 6, "a": 7}

    # Merge dict
    dict_1.update(dict_2);


    for key, item in new_dict.items():
        print("{} -> {}".format(key, item))