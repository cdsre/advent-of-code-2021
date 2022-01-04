from typing import Tuple, List


def plot_final_location(course: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    for direction, distance in course:
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    return horizontal, depth


def plot_final_with_aim(course: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    for direction, distance in course:
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    return horizontal, depth


if __name__ == "__main__":
    with open("day-2-planned-course.txt") as course_data:
        course = []
        for data in course_data.readlines():
            direction, distance = data.split()
            course.append((direction, int(distance)))

    horizontal, depth = plot_final_location(course)
    print(horizontal * depth)

    horizontal, depth = plot_final_with_aim(course)
    print(horizontal * depth)