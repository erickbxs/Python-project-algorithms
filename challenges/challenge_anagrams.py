def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def is_anagram(first_string, second_string):
    def sort_string(string):
        string = string.lower()
        return "".join(merge_sort(list(string)))

    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    if sorted_first == "" or sorted_second == "":
        return sorted_first, sorted_second, False

    return sorted_first, sorted_second, sorted_first == sorted_second
