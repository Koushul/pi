old_volume = 300
old_brightness = 183
old_offset = 0
def enlighten(volume):
    global old_volume, old_brightness, old_offset
    throttle = (volume / float(max(old_volume, 1))) - 1;
    old_brightness = int(min(max((throttle * 100 + old_brightness), 0), 255))
    old_volume = volume
    old_offset = (old_offset + 0.1) % 100;
    return spectrum(int((throttle * 33) + old_offset)) + (old_brightness,)

def spectrum(offset):
    offset = offset % 100
    red = max(getVal(offset, 0), getVal(offset, 100))
    green = getVal(offset, 33)
    blue = getVal(offset, 67)
    return (red, green, blue)

def getVal(offset, colPos):
    minO = colPos - 16.5
    maxO = colPos + 16.5
    
    if (offset > maxO):
        return max(min(255 - int(((offset - maxO) / 16.5) * 255), 255), 0)
    if (offset < minO):
        return max(min(255 - int(((minO - offset) / 16.5) * 255), 255), 0)

    return 255

