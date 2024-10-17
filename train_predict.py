import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle


import extract_v3

# Initialize feature and label lists
feature_baseline_angle = []
feature_top_margin = []
feature_letter_size = []
feature_line_spacing = []
feature_word_spacing = []
feature_pen_pressure = []
feature_slant_angle = []
labels_trait_1 = []
labels_trait_2 = []
labels_trait_3 = []
labels_trait_4 = []
labels_trait_5 = []
labels_trait_6 = []
labels_trait_7 = []
labels_trait_8 = []
page_ids = []
classifiers = []

performance_metrics = {}

# Check if label_list file exists
if os.path.isfile("label_list_mod"): # filename is modified,
    print("Info: label_list found.")
    with open("label_list_mod", "r") as labels_file: # filename is modified
        for line in labels_file:
            content = line.split()
            feature_baseline_angle.append(float(content[0]))
            feature_top_margin.append(float(content[1]))
            feature_letter_size.append(float(content[2]))
            feature_line_spacing.append(float(content[3]))
            feature_word_spacing.append(float(content[4]))
            feature_pen_pressure.append(float(content[5]))
            feature_slant_angle.append(float(content[6]))
            labels_trait_1.append(float(content[7]))
            labels_trait_2.append(float(content[8]))
            labels_trait_3.append(float(content[9]))
            labels_trait_4.append(float(content[10]))
            labels_trait_5.append(float(content[11]))
            labels_trait_6.append(float(content[12]))
            labels_trait_7.append(float(content[13]))
            labels_trait_8.append(float(content[14]))
            page_ids.append(content[15])

    # Prepare feature sets for each trait
    def prepare_feature_set(*args):
        return np.array(list(zip(*args)))

    feature_set_trait_1 = prepare_feature_set(feature_baseline_angle, feature_slant_angle)
    feature_set_trait_2 = prepare_feature_set(feature_letter_size, feature_pen_pressure)
    feature_set_trait_3 = prepare_feature_set(feature_letter_size, feature_top_margin)
    feature_set_trait_4 = prepare_feature_set(feature_line_spacing, feature_word_spacing)
    feature_set_trait_5 = prepare_feature_set(feature_slant_angle, feature_top_margin)
    feature_set_trait_6 = prepare_feature_set(feature_letter_size, feature_line_spacing)
    feature_set_trait_7 = prepare_feature_set(feature_letter_size, feature_word_spacing)
    feature_set_trait_8 = prepare_feature_set(feature_line_spacing, feature_word_spacing)

    # Define traits and their respective features
    traits = [
        ("Emotional Stability", feature_set_trait_1, labels_trait_1, 8, "poly"),
        ("Mental Energy or Will Power", feature_set_trait_2, labels_trait_2, 8, "linear"),
        ("Modesty", feature_set_trait_3, labels_trait_3, 32, "linear"),
        ("Personal Harmony and Flexibility", feature_set_trait_4, labels_trait_4, 64, "linear"),
        ("Lack of Discipline", feature_set_trait_5, labels_trait_5, 42, "sigmoid"),
        ("Poor Concentration", feature_set_trait_6, labels_trait_6, 52, "linear"),
        ("Non Communicativeness", feature_set_trait_7, labels_trait_7, 21, "poly"),
        ("Social Isolation", feature_set_trait_8, labels_trait_8, 73, "linear")
    ]

    # Function to evaluate and print metrics for each classifier
    def evaluate_classifier(features, labels, random_state, kern):
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=random_state)
        classifier = SVC(kernel=kern)
        classifier.fit(X_train, y_train)
        predictions = classifier.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions, zero_division=0)
        confusion_mat = confusion_matrix(y_test, predictions)

        return classifier, accuracy, report, confusion_mat

    # Evaluate and print results for each trait
    for trait_name, feature_set, labels, random_state, kernel in traits:
        classifier, accuracy, report, confusion_mat = evaluate_classifier(feature_set, labels, random_state, kernel)
        classifiers.append((trait_name, classifier))
        print(f"Classifier for {trait_name}")
        print(f"Accuracy: {accuracy}")
        print("Classification Report:")
        print(report)
        print("Confusion Matrix:")
        print(confusion_mat)
        print("---------------------------------------------------")

        performance_metrics[trait_name] = {
            'accuracy': accuracy,
            'classification_report': report,
            'confusion_matrix': confusion_mat.tolist()  # Convert to list for serialization
        }
        # Plotting confusion matrix
        plt.figure(figsize=(8, 6))
        sns.heatmap(confusion_mat, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(labels), yticklabels=np.unique(labels))
        plt.title(f"Confusion Matrix for {trait_name}")
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.show()

    classifier_1, classifier_2, classifier_3, classifier_4, classifier_5, classifier_6, classifier_7, classifier_8 = classifiers
    # Prediction loop for new samples
    with open('classifiers.pkl', 'wb') as f:
        pickle.dump(classifiers, f)

    with open("metrics.pkl", "wb") as f:
        pickle.dump(performance_metrics, f)

    while True:
        file_name = input("Enter file name to predict or 'z' to exit: ")
        if file_name == 'z':
            break


        raw_features = extract_v3.start(file_name)
        predictions = {
            "Emotional Stability": classifier_1.predict([[raw_features[0], raw_features[6]]]),
            "Mental Energy or Will Power": classifier_2.predict([[raw_features[2], raw_features[5]]]),
            "Modesty": classifier_3.predict([[raw_features[2], raw_features[1]]]),
            "Personal Harmony and Flexibility": classifier_4.predict([[raw_features[3], raw_features[4]]]),
            "Lack of Discipline": classifier_5.predict([[raw_features[6], raw_features[1]]]),
            "Poor Concentration": classifier_6.predict([[raw_features[2], raw_features[3]]]),
            "Non Communicativeness": classifier_7.predict([[raw_features[2], raw_features[4]]]),
            "Social Isolation": classifier_8.predict([[raw_features[3], raw_features[4]]])
        }

        for trait, prediction in predictions.items():
            print(f"{trait}: {prediction[0]}")
        print("---------------------------------------------------")

else:
    print("Error: label_list file not found.")

print("Execution was successful.")
