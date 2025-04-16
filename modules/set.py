my_set = {}

alpha_set = {
    1, 2, 3
}

super_list = [1, 2, 3, 2, 4, 5, 5, 3, 1]

# TO Set
super_set = set(super_list)

super_set.add(5);

print(super_set)

to_list = list(super_set)

print(to_list)


# UNION
superx = super_set.intersection(alpha_set)
print(f"IOX: {superx}")
print(super_set.difference(alpha_set))