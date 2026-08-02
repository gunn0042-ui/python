import string

# Function to count word frequency
def word_frequency(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count word frequencies
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Sort by frequency (highest first)
    top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Return top 3 words
    return top_words[:3]


# Test text
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

# Display results
print("Top 3 words:")
result = word_frequency(text)

for word, count in result:
    print(f"{word} — {count} times")