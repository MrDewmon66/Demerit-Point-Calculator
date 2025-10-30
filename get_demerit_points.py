# Lab 13-1-1, Question 1
# Aayden Cameron, ajc0698@arastudent.ac.nz

def get_demerit_points(driving_speed: int|float, speed_limit: int, holiday_period: bool = False) -> tuple:
    """Gets the demerit points from the given speed in relation to the speed limit.

    Args:
        driving_speed (int or float): The driving speed
        speed_limit (int): The speed limit
        holiday_period (bool, optional): Whether its a holiday period or not. Defaults to False.

    Returns:
        tuple: _description_
    """
    if driving_speed > (speed_limit + 4) and holiday_period:
        mandotory_penalty = True
    elif driving_speed > (speed_limit + 5) and not holiday_period:
        mandotory_penalty = True
    else:
        mandotory_penalty = False

    if driving_speed <= speed_limit:
        return (mandotory_penalty, 0)
    elif driving_speed <= (speed_limit + 10):
        return (mandotory_penalty, 10)
    elif driving_speed > (speed_limit + 10) and driving_speed <= (speed_limit + 20):
        return (mandotory_penalty, 20)
    elif driving_speed > (speed_limit + 20) and driving_speed <= (speed_limit + 30):
        return (mandotory_penalty, 30)
    elif driving_speed > (speed_limit + 30):
        return (mandotory_penalty, 50)
    
# Test 20km/h speed limit
if __name__ == "__main__":
    HOLIDAY_COMBINATIONS = (True, False)
    speed_limits = (20,)
    speed_differences = (-1, 0, 1, 4, 4.5, 5, 5.2, 9, 9.1, 10, 11, 20, 20.3, 21, 29, 30, 31, 40)

    for speed_limit in speed_limits:
        for speed_offset in speed_differences:
                actual_speed = speed_limit + speed_offset
                for holiday in HOLIDAY_COMBINATIONS:
                    points = get_demerit_points(driving_speed=actual_speed, speed_limit=speed_limit, holiday_period=holiday)
                    print(f'Driving {actual_speed:>4}km/h in a {speed_limit:>3}km/h zone '\
                        f"{'during a holiday period' if bool(holiday) else 'not in a holiday period'} "\
                        f"is {points[1]:>2} {'mandatory' if points[0] else 'optional '} points")