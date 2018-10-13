def calculateFootprint(mpg, dist):
    # calculate the carbon emissions released while traveling the given
    # distance
    emission = "%.1f" % float(float(dist) / float(mpg) * 20.0)
    return emission

def numTravelsInYear(emission):
    # the number of travels to given place one would complete in a year to get
    # the average per-capita carbon emissions in the U.S.
    travels = "%.1f" % float(float(16.491 * 2204.62) / float(emission))
    return travels

def numTravelsInMonth(emission):
    # the number of travels to given place one would complete in a month to get
    # the average per-capita carbon emissions in the U.S.
    travels = "%.1f" % float(float(1.374 * 2204.62) / float(emission))
    return travels