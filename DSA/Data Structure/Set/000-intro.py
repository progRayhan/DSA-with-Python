set_one = {1,2,3,4} # only contains unique value
print(set_one)

set_two = {1,1,2,2,3,4} # duplicate value are ignored
print(set_two)

is_set_one_and_two_are_equal = (set_one == set_two)
print(is_set_one_and_two_are_equal)

set_one.add(50) # mutable
print(set_one)

demo_set = set()
demo_set.add(5)
demo_set.add(10)
print(demo_set) # Sorting Values from Low to High
