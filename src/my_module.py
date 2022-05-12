import datetime


def get_cheapest_hotel(number):  # DO NOT change the function's name

    number = number.replace(":", " ").replace(",", " ").replace("(", "").replace(")", "")
    info = number.split()

    client_type = [info[0]]

    info.pop(0)

    date_time = info

    value_lakewood = []
    value_bridgewood = []
    value_ridgewood = []

    for i in range(len(date_time)):
        cheapest_hotel = convert(date_time[0 + i], client_type, value_lakewood, value_bridgewood, value_ridgewood)

    return cheapest_hotel


def convert(date_time, client_type, value_lakewood, value_bridgewood, value_ridgewood):
    date_format = '%d%b%Y%a'
    try:
        date = datetime.datetime.strptime(date_time, date_format)
    except:
        additional_character = date_time.rindex(date_time[-1])
        date_time = date_time[:additional_character:]
        date = datetime.datetime.strptime(date_time, date_format)

    lakewood = [3, 110, 80, 90, 80]
    bridgewood = [4, 160, 110, 60, 50]
    ridgewood = [5, 220, 100, 150, 40]

    if date.isoweekday() <= 5:

        if "Regular" in client_type:
            value_lakewood.append(lakewood[1])
            value_bridgewood.append(bridgewood[1])
            value_ridgewood.append(ridgewood[1])

        if "Rewards" in client_type:
            value_lakewood.append(lakewood[2])
            value_bridgewood.append(bridgewood[2])
            value_ridgewood.append(ridgewood[2])

    else:

        if "Regular" in client_type:
            value_lakewood.append(lakewood[3])
            value_bridgewood.append(bridgewood[3])
            value_ridgewood.append(ridgewood[3])

        if "Rewards" in client_type:
            value_lakewood.append(lakewood[4])
            value_bridgewood.append(bridgewood[4])
            value_ridgewood.append(ridgewood[4])

    if sum(value_bridgewood) < sum(value_lakewood) and sum(value_bridgewood) < sum(value_ridgewood):
        return "Bridgewood"
    elif sum(value_lakewood) < sum(value_bridgewood) and sum(value_lakewood) < sum(value_ridgewood):
        return "Lakewood"
    else:
        return "Ridgewood"
