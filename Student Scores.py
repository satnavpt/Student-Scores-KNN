import random
from operator import itemgetter
from statistics import mode

all_scores = [["A0", 9, 3], ["A1", 2, 6], ["A2", 9, 4], ["A3", 7, 3], ["A4", 8, 5], ["A5", 9, 3], ["A6", 8, 2], ["A7", 7, 4], ["A8", 6, 5], ["A9", 9, 2], ["B0", 4, 3], ["B1", 5, 8], ["B2", 6, 9], ["B3", 3, 9], ["B4", 4, 9], ["B5", 5, 9], ["B6", 6, 7], ["B7", 3, 8], ["B8", 4, 8], ["B9", 4, 9]]
y = 0

while y < 50:

    overall = []
    x = 0

    while x < 100:

        ### Let there be two classes of students, class A and class B
        ### Let each student in the class have a score out 10 for maths and for english
        ### Let class A have better scores for maths and class B have better scores for english
        ### Let x be the class and student number, y be the score for maths and z be the score for english

        training_scores = random.sample(all_scores, 19)

        for item in all_scores:
            if item not in training_scores:
                testing_score = item

        #for test_score in testing_scores:
        #    distances = []
        #    test_x, test_y = item[1], item[2]

        distances = []
        test_class = testing_score[0]
        test_x, test_y = testing_score[1], testing_score[2]

        for train_score in training_scores:
            train_class, train_x, train_y = train_score[0], train_score[1], train_score[2]
            distance = ((train_x-test_x)**2 + (train_y-test_y)**2)**0.5
            distances.append([distance, test_class, train_class])

        distances = sorted(distances, key=itemgetter(0))[:5]
        nearest_class = []
        for distance in distances:
            nearest_class.append(distance[2][0])

        suggested_class = mode(nearest_class)

        #print(all_scores)
        #print(training_scores)
        #print(testing_score)
        #print(distances)
        #print(nearest_class)
        #print(suggested_class)
        if suggested_class == test_class[0]:
            overall.append(["correct", test_class])
        else:
            overall.append(["incorrect", test_class])

        x+=1

    outcomes = []
    possible_outliers = []
    for item in overall:
        outcomes.append(item[0])

    for item in overall:
        if item[0] == "incorrect":
            possible_outliers.append(item[1])

    accuracy = (str(outcomes.count("correct")/len(outcomes)*100) + "%")
    print("The accuracy of this test was", accuracy)

    if possible_outliers:
        possible_outlier = mode(possible_outliers)
        print(possible_outlier, "is a possible outlier")
        choice = input("Should this item be removed from the training data?  ")
        if choice == "yes":
            if possible_outlier[0] == "A":
                all_scores.remove(all_scores[int(possible_outlier[1])])
            else:
                all_scores.remove(all_scores[int(possible_outlier[1]) + 10])
            print(all_scores)
            print("repeating")
        else:
            print("repeating")
    else:
        print("There were no outliers")
        print("repeating")

    y += 1
