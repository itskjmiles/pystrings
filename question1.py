# Task 1
def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)

# Task 2
def count_sentiments(review):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_count = sum(1 for word in review.split() if word.lower() in positive_words)
    negative_count = sum(1 for word in review.split() if word.lower() in negative_words)
    return positive_count, negative_count

# Task 3
def generate_summary(review):
    max_length = 30
    if len(review) <= max_length:
        return review
    else:
        space_index = review.rfind(" ", 0, max_length)
        if space_index != -1:
            return review[:space_index] + "…"
        else:
            return review[:max_length] + "…"

def main():
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

    print("Task 1: Keyword Highlighter")
    highlight_keywords(reviews)

    print("\nTask 2: Sentiment Tally")
    for review in reviews:
        positive_count, negative_count = count_sentiments(review)
        print(f"Review: {review}")
        print(f"Positive Words: {positive_count}, Negative Words: {negative_count}")

    print("\nTask 3: Review Summary")
    for review in reviews:
        summary = generate_summary(review)
        print(f"Review: {review}")
        print(f"Summary: {summary}")

if __name__ == "__main__":
    main()
