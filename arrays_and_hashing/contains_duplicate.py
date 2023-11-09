"""
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct. 

"""

# solution


def containsDuplicate(arr):

    unique_subset_for_input_array = set(arr)

    if (len(unique_subset_for_input_array) == len(arr)):
        return False
    else:
        return True


# second solution

def containsDuplicate2(arr):

    checked = dict()

    for i in arr:

        try:
            if checked[i] == True:
                return True
        except KeyError:
            checked[i] = True

    return False
