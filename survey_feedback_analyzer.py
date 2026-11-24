
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print(feedback_data)

# Step 2: Add More Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter Feedback Details")

    name = input("Enter Name: ")
    feedback = input("Enter Feedback: ")
    rating = int(input("Enter Rating (1-5): "))

    while rating < 1 or rating > 5:
        print("Please enter rating between 1 and 5")
        rating = int(input("Enter Rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nUpdated Feedback Data:")
print(feedback_data)

# Step 3: Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    text = ' '.join(text.split())

    text = text.lower()

    feedback_data['Feedback'][i] = text

print("\nCleaned Feedback Data:")
print(feedback_data['Feedback'])

# Step 4: Word Count Insights

def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        words = feedback.lower().split()

        if word.lower() in words:
            count += 1

    return count


print("\nWord Count Insights:")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))

# Step 5: Final Summary and Insights

# Display Final Cleaned Feedback Data
print("\nFinal Cleaned Feedback Data:")
print(feedback_data)


# Calculate Average Rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])

print("\nAverage Rating:", round(average_rating, 2))


# Find Feedback with Longest Comment
longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda x: len(x.split())
)

print("\nLongest Feedback:")
print(longest_feedback)

print("Word Count:", len(longest_feedback.split()))


# Find Unique Words
unique_words = set()

for feedback in feedback_data['Feedback']:
    words = feedback.split()
    for word in words:
        unique_words.add(word)

print("\nUnique Words:")
print(sorted(unique_words))

print("\nTotal Unique Words:", len(unique_words))

# Optional: Sort Feedbacks by Rating

sorted_feedbacks = sorted(
    zip(feedback_data['Rating'],
        feedback_data['Name'],
        feedback_data['Feedback']),
    reverse=True
)

print("\nFeedbacks Sorted by Rating (Highest to Lowest):")

for rating, name, feedback in sorted_feedbacks:
    print(name, "| Rating:", rating, "| Feedback:", feedback)
