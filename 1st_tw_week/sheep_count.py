def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)

def find_needle(haystack):
    if "needle" in haystack:
        index =  haystack.index("needle")
    return ("found the needle at position { }".format(index))

