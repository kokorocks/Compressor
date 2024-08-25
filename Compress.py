import re

def compress(text):
    # Find all patterns of consecutive repeated characters
    pattern = re.compile(r'(.)\1*')
    compressed = []

    for match in pattern.finditer(text):
        char = match.group(1)
        count = len(match.group(0))
        compressed.append(f'{char}{count}')

    return ''.join(compressed)

def decompress(compressed_text):
    # Decompress the text
    decompressed = []
    i = 0

    while i < len(compressed_text):
        char = compressed_text[i]
        count = 0

        # Move to the next character which should be a digit
        i += 1
        while i < len(compressed_text) and compressed_text[i].isdigit():
            count = count * 10 + int(compressed_text[i])
            i += 1

        decompressed.append(char * count)

    return ''.join(decompressed)

# Example usage
original_text = "aaabbbcccaaa"
compressed_text = compress(original_text)
decompressed_text = decompress(compressed_text)

print("Original:", original_text)
print("Compressed:", compressed_text)
print("Decompressed:", decompressed_text)
