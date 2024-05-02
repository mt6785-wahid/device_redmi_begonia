import sys

def organize_file(file_path):
    try:
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Create a list to store the sections
        sections = []

        # Create a dictionary to store the lines by section
        section_lines = {}
        current_section = None

        # Iterate over the lines and group them by section
        for line in lines:
            if line.startswith('#'):  # Assuming sections start with a '#' character
                if current_section:
                    sections.append(current_section)
                current_section = line.strip()
                section_lines[current_section] = []
            else:
                section_lines[current_section].append(line)

        if current_section:
            sections.append(current_section)

        # Sort the sections alphabetically
        sections.sort()

        # Write the sorted sections and their lines to a new file
        with open('sorted_' + file_path, 'w') as sorted_file:
            for section in sections:
                sorted_file.write(section)
                sorted_lines = sorted(section_lines[section], key=lambda x: x.lower())
                unique_lines = set()
                duplicated_lines = set()
                for line in sorted_lines:
                    if line in unique_lines:
                        duplicated_lines.add(line)
                    else:
                        unique_lines.add(line)
                        sorted_file.write(line)
                sorted_file.write('\n')  # Add a new line after the last line in each section

                if duplicated_lines:
                    print(f"Duplicated lines found in section '{section}':")
                    for line in duplicated_lines:
                        print(line.strip())
                    print()
                    print("Successfully removed duplicated lines") 

        print("File organized successfully. Sorted file saved as 'sorted_" + file_path + "'.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Check if a file path was provided as a command-line argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    organize_file(file_path)
else:
    print("Please provide the path to the file you want to organize as a command-line argument.")
