import json
from functools import reduce
from typing import List, Tuple


def decode_value(base: int, value: str) -> int:
    """Decode the value from the given base to decimal."""
    return int(value, base)


def lagrange_interpolation(points: List[Tuple[int, int]]) -> int:
    """Calculate the constant term of the polynomial using Lagrange interpolation."""
    secret = 0
    n = len(points)

    for i in range(n):
        xi, yi = points[i]
        li = reduce(lambda acc, j: acc * (xi - points[j][0]) / (xi - points[j][0]) if j != i else acc, range(n), 1)
        secret += yi * li

    return int(secret) % (2 ** 256)  # Considering the range of coefficients as specified


def main():
    # Read the input from a JSON file
    with open('input.json', 'r') as file:
        data = json.load(file)

    n = data['keys']['n']
    k = data['keys']['k']

    points = []

    # Decode the Y values and construct the points
    for key in data.keys():
        if key != 'keys':
            base = int(data[key]['base'])
            value = data[key]['value']
            decoded_value = decode_value(base, value)
            points.append((int(key), decoded_value))

    # Calculate the constant term 'c'
    constant_term = lagrange_interpolation(points[:k])  # Use only the first k points for interpolation
    print(f"The secret (constant term c) is: {constant_term}")


if __name__ == "__main__":
    main()
