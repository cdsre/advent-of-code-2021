from typing import List


def get_total_increases(numbers: List[int]) -> int:
    total_increase = 0
    previous = numbers[0]
    for num in numbers[1:]:
        if num > previous:
            total_increase += 1
        previous = num

    return total_increase


def get_sliding_window_increases(numbers: List[int]) -> int:
    total_increase = 0
    previous = sum(numbers[0:3])
    for i in range(1, len(numbers)):
        window = sum(numbers[i:i + 3])
        if window > previous:
            total_increase += 1
        previous = window

    return total_increase


def get_increase_for_n_window(numbers: List[int], window=1) -> int:
    total_increase = 0
    previous = sum(numbers[0:window])
    for i in range(1, len(numbers)):
        window = sum(numbers[i:i + window])
        if window > previous:
            total_increase += 1
        previous = window

    return total_increase


if __name__ == "__main__":
    with open("numbers_input_data.txt") as numbers_data:
        numbers = [int(num) for num in numbers_data.readlines()]
    print(get_total_increases(numbers))
    print(get_sliding_window_increases(numbers))
