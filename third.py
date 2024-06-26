def main():
    heights_inches = []
    heights_cm = []

    while True:
        height_inch_str = input("Enter height in inches (or 'q' to quit): ")
        if height_inch_str.lower() == 'q':
            break
        try:
            height_inch = float(height_inch_str)
            heights_inches.append(height_inch)

            height_cm = height_inch * 2.54
            heights_cm.append(height_cm)
        except ValueError:
            print("Invalid input.")

    print("\nHeights in inches:", heights_inches)
    print("Heights in centimeters (loop):", heights_cm)

    heights_cm_comprehension = [round(inch * 2.54, 2) for inch in heights_inches]
    print("Heights in centimeters (comprehension):", heights_cm_comprehension)

main()
