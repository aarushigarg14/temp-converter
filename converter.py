def convert(value, scale):
    if scale == "C":
        return (value * 9/5) + 32   # This line will be changed in both branches
    elif scale == "F":
        return (value - 32) * 5/9   # This line will also be changed differently
    else:
        return "Invalid scale"
