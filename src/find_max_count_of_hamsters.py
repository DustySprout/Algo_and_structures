def check_feeding_hamsters(hamsters, sum_of_eat):
    sum_food_for_all_hamsters = sum(sorted([hamster[0] + hamster[1] * len(hamsters) for hamster in hamsters]))
    if sum_food_for_all_hamsters <= sum_of_eat:
        return True


def max_hamsters_count_with_dividings(start_index, end_index, sum_of_eat, count_of_food_for_different_count_of_hamsters, hamsters):
    middle_index = (start_index + end_index) // 2
    food_needed_list = sorted([hamster[0] + hamster[1] * middle_index for hamster in hamsters])
    sum_of_food_needed_list_to_middle_index = sum(food_needed_list[:middle_index + 1])
    if sum_of_food_needed_list_to_middle_index == sum_of_eat:
        return middle_index + 1

    elif sum_of_food_needed_list_to_middle_index > sum_of_eat:
        count_of_food_for_different_count_of_hamsters[middle_index] = sum_of_food_needed_list_to_middle_index
        return max_hamsters_count_with_dividings(start_index, middle_index - 1, sum_of_eat, count_of_food_for_different_count_of_hamsters, hamsters)


    else:
        count_of_food_for_different_count_of_hamsters[middle_index] = sum_of_food_needed_list_to_middle_index
        if middle_index + 1 > len(count_of_food_for_different_count_of_hamsters) - 1:
            return middle_index + 1
        if count_of_food_for_different_count_of_hamsters[middle_index + 1] > sum_of_eat:
            return middle_index + 1
        else:
            return max_hamsters_count_with_dividings(middle_index + 1, end_index, sum_of_eat, count_of_food_for_different_count_of_hamsters, hamsters)


def max_hamsters(sum_of_eat, count_of_hamsters, hamsters):
    check_data_validity(sum_of_eat, count_of_hamsters)
    count_of_food_for_different_count_of_hamsters = [0] * count_of_hamsters
    if check_feeding_hamsters(hamsters, sum_of_eat):
        return count_of_hamsters
    return max_hamsters_count_with_dividings(0, count_of_hamsters - 1, sum_of_eat,
                                             count_of_food_for_different_count_of_hamsters, hamsters)


def check_data_validity(sum_of_eat, count_of_hamsters):
    if not 0 <= sum_of_eat <= 10 ** 9:
        raise ValueError("sum_of_eat must be between 0 and 10^9")
    if not 1 <= count_of_hamsters <= 10 ** 5:
        raise ValueError("count_of_hamsters must be between 1 and 10^5")
