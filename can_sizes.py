import math
data = {
    '#1 Picnic': {'radius': 6.83, 'height': 10.16, 'cost': 0.28},
    '#1 Tall': {'radius': 7.78, 'height': 11.91, 'cost': 0.43},
    '#2': {'radius': 8.73, 'height': 11.59, 'cost': 0.45},
    '#2.5': {'radius': 10.32, 'height': 11.91, 'cost': 0.61},
    '#3 Cylinder': {'radius': 10.79, 'height': 17.78, 'cost': 0.86},
    '#5': {'radius': 13.02, 'height': 14.29, 'cost': 0.83},
    '#6Z': {'radius': 5.40, 'height': 8.89, 'cost': 0.22},
    '#8Z short': {'radius': 6.83, 'height': 7.62, 'cost': 0.26},
    '#10': {'radius': 15.72, 'height': 17.78, 'cost': 1.53},
    '#211': {'radius': 6.83, 'height': 12.38, 'cost': 0.34},
    '#300': {'radius': 7.62, 'height': 11.27, 'cost': 0.38},
    '#303': {'radius': 8.10, 'height': 11.11, 'cost': 0.42}
}

# for top, nested in data.items():
#     print(f"{top}")
#     for nested_key, v in nested.items():
#         print(f"k: {nested_key}, v: {v}")


def main():
    for key, keys in data.items():
        r = ''
        h = ''
        if 'radius' in keys:
            r = keys['radius']
        if 'height' in keys:
            h = keys['height']
        v = compute_volume(r, h)
        s = compute_surface_area(r, h)
        efficiency = compute_storage_efficiency(v, s)
        print(f"{key} {efficiency:.2f}")


def compute_volume(r, h):
    return math.pi * (r ** 2) * h


def compute_surface_area(r, h):
    return 2 * math.pi * r * (r + h)


def compute_storage_efficiency(v, s):
    return v / s


main()
