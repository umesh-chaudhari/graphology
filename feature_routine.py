import os
import categorize

if os.path.isfile("processed_features"):
    print("Error: processed_features already exists.")

elif os.path.isfile("raw_data"):
    print("Info: raw data found.")
    with open("raw_data", "r") as raw_data_file, open("processed_features", "a") as features_file:
        for line in raw_data_file:
            data_points = line.split()

            raw_angle = float(data_points[0])
            raw_margin = float(data_points[1])
            raw_size = float(data_points[2])
            raw_spacing_vertical = float(data_points[3])
            raw_spacing_horizontal = float(data_points[4])
            raw_pressure = float(data_points[5])
            raw_slant = float(data_points[6])
            page_identifier = data_points[7]

            angle, comment = categorize.determine_baseline_angle(raw_angle)
            margin, comment = categorize.determine_top_margin(raw_margin)
            size, comment = categorize.determine_letter_size(raw_size)
            line_spacing, comment = categorize.determine_line_spacing(raw_spacing_vertical)
            word_spacing, comment = categorize.determine_word_spacing(raw_spacing_horizontal)
            pressure, comment = categorize.determine_pen_pressure(raw_pressure)
            slant, comment = categorize.determine_slant_angle(raw_slant)

            features_file.write(f"{angle}\t{margin}\t{size}\t{line_spacing}\t{word_spacing}\t{pressure}\t{slant}\t{page_identifier}\t")
            print(features_file, '')
    print("Done!")

else:
    print("Error: raw data file not found.")
