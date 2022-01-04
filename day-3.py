def conumption(binary_data: List[str]) -> Tuple[str, str]

if __name__ == "__main__":
    with open("day-3-diagnostic.txt") as diagnostic_data:
        binary_data = [data.strip() for data in diagnostic_data.readlines()]
        print(binary_data)