def convert(value, scale):
    if scale == "C":
        return (value * 9/5) + 32
    elif scale == "F":
        return (value - 32) * 5/9   
    else:
        return "Invalid scale"
