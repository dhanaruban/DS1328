Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
                       "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
                       "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                       "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                       "Magical Mystery Tour": 1967, "The Beatles": 1968,
                       "Yellow Submarine": 1969, 'Abbey Road': 1969,
                       "Let It Be": 1970}


def most_prolific(dict_input):
    year = {}
    for value in dict_input.values():
        if value in year:
            year[value] += 1
        else:
            year[value] = 1
    max_count_year = 0
    max_year = 0
    for item in year.keys():
        if year[item] > max_count_year:
            max_year = item
            max_count_year = year[item]

    return max_year


print(most_prolific(Beatles_Discography))