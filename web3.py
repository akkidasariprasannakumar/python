positive_words = [
    "good", "excellent", "helpful", "great",
    "interesting", "clear", "best", "useful",
    "wonderful", "friendly"
]

negative_words = [
    "bad", "poor", "boring", "difficult",
    "confusing", "worst", "unclear",
    "unhelpful", "slow", "disappointing"
]

# Input multiple feedback sentences
n = int(input("Enter number of feedback sentences: "))

for i in range(n):
    feedback = input(f"\nEnter feedback {i + 1}: ").lower()

    # Split sentence into words
    words = feedback.split()

    positive_count = 0
    negative_count = 0

    # Count positive and negative keywords
    for word in words:
        word = word.strip(".,!?;:")

        if word in positive_words:
            positive_count += 1

        if word in negative_words:
            negative_count += 1

    # Calculate sentiment score
    score = positive_count - negative_count

    # Classify the feedback
    if score >= 2:
        sentiment = "Positive"
    elif score <= -2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Display results
    print("\n--- Feedback Analysis ---")
    print("Feedback:", feedback)
    print("Positive indicators:", positive_count)
    print("Negative indicators:", negative_count)
    print("Sentiment score:", score)
    print("Classification:", sentiment)
    print("-" * 30)
