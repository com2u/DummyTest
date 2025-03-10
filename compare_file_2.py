 compare_file_2.py

def compare_lists(list1, list2):
    """
    Compares two lists and returns the differences.
    
    Args:
    list1 (list): The first list to compare.
    list2 (list): The second list to compare.
    
    Returns:
    tuple: A tuple containing items unique to list1 and items unique to list2.
    """
    unique_to_list1 = set(list1) - set(list2)
    unique_to_list2 = set(list2) - set(list1)
    return (unique_to_list1, unique_to_list2)

if __name__ == "__main__":
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    differences = compare_lists(list_a, list_b)
    print("Unique to list A:", differences[0])
    print("Unique to list B:", differences[1])