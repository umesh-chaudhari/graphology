def determine_baseline_angle(raw_angle):
    comment = ""
    if raw_angle >= 0.2:  # falling
        angle_category = 0
        comment = "DESCENDING"
    elif raw_angle <= -0.3:  # rising
        angle_category = 1
        comment = "ASCENDING"
    else:  # straight
        angle_category = 2
        comment = "STRAIGHT"
    return angle_category, comment


def determine_top_margin(raw_margin):
    comment = ""
    if raw_margin >= 1.7:  # medium and bigger
        margin_category = 0
        comment = "MEDIUM OR BIGGER"
    else:  # narrow
        margin_category = 1
        comment = "NARROW"
    return margin_category, comment


def determine_letter_size(raw_size):
    comment = ""
    if raw_size >= 18.0:  # big
        size_category = 0
        comment = "BIG"
    elif raw_size < 13.0:  # small
        size_category = 1
        comment = "SMALL"
    else:  # medium
        size_category = 2
        comment = "MEDIUM"
    return size_category, comment


def determine_line_spacing(raw_spacing):
    comment = ""
    if raw_spacing >= 3.5:  # big
        spacing_category = 0
        comment = "BIG"
    elif raw_spacing < 2.0:  # small
        spacing_category = 1
        comment = "SMALL"
    else:  # medium
        spacing_category = 2
        comment = "MEDIUM"
    return spacing_category, comment


def determine_word_spacing(raw_spacing):
    comment = ""
    if raw_spacing > 2.0:  # big
        spacing_category = 0
        comment = "BIG"
    elif raw_spacing < 1.2:  # small
        spacing_category = 1
        comment = "SMALL"
    else:  # medium
        spacing_category = 2
        comment = "MEDIUM"
    return spacing_category, comment


def determine_pen_pressure(raw_pressure):
    comment = ""
    if raw_pressure > 180.0:  # heavy
        pressure_category = 0
        comment = "HEAVY"
    elif raw_pressure < 151.0:  # light
        pressure_category = 1
        comment = "LIGHT"
    else:  # medium
        pressure_category = 2
        comment = "MEDIUM"
    return pressure_category, comment


def determine_slant_angle(raw_angle):
    comment = ""
    if raw_angle in [-45.0, -30.0]:  # extremely reclined
        angle_category = 0
        comment = "EXTREMELY RECLINED"
    elif raw_angle in [-15.0, -5.0]:  # a little or moderately reclined
        angle_category = 1
        comment = "A LITTLE OR MODERATELY RECLINED"
    elif raw_angle in [5.0, 15.0]:  # a little inclined
        angle_category = 2
        comment = "A LITTLE INCLINED"
    elif raw_angle == 30.0:  # moderately inclined
        angle_category = 3
        comment = "MODERATELY INCLINED"
    elif raw_angle == 45.0:  # extremely inclined
        angle_category = 4
        comment = "EXTREMELY INCLINED"
    elif raw_angle == 0.0:  # straight
        angle_category = 5
        comment = "STRAIGHT"
    else:  # irregular
        angle_category = 6
        comment = "IRREGULAR"
    return angle_category, comment
