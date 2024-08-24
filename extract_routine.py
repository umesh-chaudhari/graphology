import os
import extract_v3

# Change working directory to 'images'
os.chdir("images")
# List all files in the current directory
image_files = [file for file in os.listdir('.') if os.path.isfile(file)]
# Change back to the previous directory
os.chdir("..")

page_ids = []
# Check if 'raw_feature_list' file exists
if os.path.isfile("raw_feature_list"):
    print("Info: 'raw_feature_list' already exists.")
    with open("raw_feature_list", "r") as file:
        for line in file:
            content = line.split()
            page_id = content[-1]
            page_ids.append(page_id)

with open("raw_feature_list", "a") as file:
    processed_count = len(page_ids)
    for image_file in image_files:
        if image_file in page_ids:
            continue
        features = extract_v3.start(image_file)
        features.append(image_file)
        for feature in features:
            file.write("%s\t" % feature)
        file.write('\n')
        processed_count += 1
        progress = (processed_count * 100) / len(image_files)
        print(f"{processed_count} {image_file} {progress}%")
    print("Done!")
