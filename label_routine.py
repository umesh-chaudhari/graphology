# this file actually calculates what trait to be classified in the context of given parameters

import os


def determine_emotional_stability(baseline_angle, slant_angle):
    if slant_angle == 0 or baseline_angle == 0:
        return 0
    elif 4 < slant_angle < 6:
        return 1
    else:
        return 2


def determine_mental_energy(letter_size, pen_pressure):
    # mental_energy = 1 = high or average, 0 = low
    if (pen_pressure == 1) or (letter_size == 1):
        return 1
    elif pen_pressure == 2 or letter_size == 2:
        return 2
    else:
        return 0


def determine_modesty(top_margin, letter_size):
    # modesty = 1 = observed, 0 = not observed (not necessarily the opposite)
    if top_margin == 0:
        return 1
    elif letter_size == 1:
        return 2
    else:
        return 0


def determine_personal_harmony(line_spacing, word_spacing):
    # personal_harmony = 1 = harmonious, 0 = non harmonious
    if line_spacing == 2 and word_spacing == 2:
        return 2
    elif line_spacing == 1 or word_spacing == 1:
        return 1
    else:
        return 0


def determine_lack_of_discipline(top_margin, slant_angle):
    # lack_of_discipline = 1 = observed, 0 = not observed (not necessarily the opposite)
    if (top_margin == 1 and slant_angle == 6):
        return 2
    elif top_margin == 1 or slant_angle < 6:
        return 1
    else:
        return 0


def determine_concentration_power(letter_size, line_spacing):
    # concentration_power = 1 = observed, 0 = not observed (not necessarily the opposite)
    if letter_size == 0 and line_spacing == 1:
        return 2
    elif line_spacing == 0:
        return 1
    else:
        return 0


def determine_communicativeness(letter_size, word_spacing):
    # communicativeness = 1 = observed, 0 = not observed (not necessarily the opposite)
    if letter_size == 1 and word_spacing == 0:
        return 2
    elif letter_size == 0:
        return 1
    else:
        return 0


def determine_social_isolation(line_spacing, word_spacing):
    # social_isolation = 1 = observed, 0 = not observed (not necessarily the opposite)
    if word_spacing == 0 or line_spacing == 0:
        return 2
    elif line_spacing == 1:
        return 1
    else:
        return 0


if os.path.isfile("label_list_mod"):
    print("Error: label_list already exists.")

elif os.path.isfile("feature_list"):
    print("Info: feature_list found.")
    with open("feature_list", "r") as features, open("label_list_mod", "a") as labels:
        for line in features:
            content = line.split()

            baseline_angle = float(content[0])
            top_margin = float(content[1])
            letter_size = float(content[2])
            line_spacing = float(content[3])
            word_spacing = float(content[4])
            pen_pressure = float(content[5])
            slant_angle = float(content[6])
            page_id = content[7]

            # Determine traits based on features
            emotional_stability = determine_emotional_stability(baseline_angle, slant_angle)
            mental_energy = determine_mental_energy(letter_size, pen_pressure)
            modesty = determine_modesty(top_margin, letter_size)
            personal_harmony = determine_personal_harmony(line_spacing, word_spacing)
            lack_of_discipline = determine_lack_of_discipline(top_margin, slant_angle)
            concentration_power = determine_concentration_power(letter_size, line_spacing)
            communicativeness = determine_communicativeness(letter_size, word_spacing)
            social_isolation = determine_social_isolation(line_spacing, word_spacing)

            labels.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
                str(baseline_angle), str(top_margin), str(letter_size),
                str(line_spacing), str(word_spacing), str(pen_pressure), str(slant_angle)))
            labels.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
                str(emotional_stability), str(mental_energy), str(modesty),
                str(personal_harmony), str(lack_of_discipline), str(concentration_power),
                str(communicativeness), str(social_isolation)))
            labels.write("%s" % str(page_id))
            labels.write('\n')
    print("Done!")

else:
    print("Error: feature_list file not found.")
