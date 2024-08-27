import string

# Open the file in read mode
text = open("sample.txt", "r")

# Initialize an empty dictionary
d = dict()

# Process each line in the file
for line in text:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Convert the line to lowercase
    line = line.lower()
    # Remove punctuation using str.translate
    line = line.translate(str.maketrans("", "", string.punctuation))
    # Split the line into words
    words = line.split()

    # Count each word
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Display the word frequency
for key in sorted(d):
    print(f'{key}: {d[key]}')
