def main():
    rain_chances = [10, 0, 20, 50, 90]
    if is_going_to_rain(rain_chances):
        print("It is going to rain")
    else:
        print("It wont rain")


def is_going_to_rain(rain_chances):
    """Determine if it will rain based on rain chances"""
    rain_chance = [rain_chance for rain_chance in rain_chances if rain_chance >= 50]
    if len(rain_chance) >= 1:
        return True
    return False


if __name__ == '__main__':
    main()

