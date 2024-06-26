def main():
    input_file = "input.txt"
    output_file = "output.txt"
    word_counts = {}

    try:
        with open(input_file, "r") as file:
            for line in file:
                words = line.strip().split()

                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1

                print(line.strip(), "Word_Count:", ", ".join(f"{word}: {count}" for word, count in word_counts.items()))

        with open(output_file, "w") as outfile:
            for line in word_counts:
                outfile.write(f"{line}: {word_counts[line]}\n")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

main()
