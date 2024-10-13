import csv

def txt_to_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as txt_file:
            lines = txt_file.readlines()

        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Number'])  # CSV header

            for line in lines:
                number = line.strip()
                if number:  # If the line is not empty
                    writer.writerow([number])

        print(f"Successfully converted {input_file} to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
txt_to_csv('test_case_1-1.txt', 'test_case_1-1.csv')
txt_to_csv('test_case_2.txt', 'test_case_2.csv')
txt_to_csv('test_case_3.txt', 'test_case_3.csv')