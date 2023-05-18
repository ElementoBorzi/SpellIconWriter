import os
import csv
import sys

def read_csv(csv_path):
    data = []
    last_id = 0
    try:
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # skip the headers
            for row in reader:
                data.append(row[1].replace('Interface\\Icons\\', ''))
                last_id = int(row[0])
    except FileNotFoundError:
        pass
    return data, last_id

def write_to_csv(csv_path, new_data):
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        if not file_exists:
            writer.writerow(["ID","TextureFilename", ""])  # write header if file not exists
        # Append an empty string to each row
        new_data_with_trailing_comma = [row + [""] for row in new_data]
        writer.writerows(new_data_with_trailing_comma)

def main():
    # Set the directory and CSV file paths here
    directory_path = r"C:\Icons Blizz\interface\icons"
    csv_path = r"C:\DBCtoCSV\SpellIcon.csv"
    
    existing_files, last_id = read_csv(csv_path)

    new_data = []
    all_files = os.listdir(directory_path)
    blp_files = [f for f in all_files if f.endswith('.blp')]
    total_files = len(blp_files)
    
    for i, filename in enumerate(blp_files, start=1):
        # Remove .blp extension from filename
        filename_without_ext = os.path.splitext(filename)[0]
        if filename_without_ext not in existing_files:
            last_id += 1
            # Prepend the path to the filename
            new_data.append([last_id, f'Interface\\Icons\\{filename_without_ext}'])
        print(f'Processed file {i} of {total_files} ({filename})')
        progress = (i / total_files) * 100
        sys.stdout.write(f'\rProgress: {progress:.2f}%')
        sys.stdout.flush()
    
    write_to_csv(csv_path, new_data)

    input("\n\nPress enter to close...")
    print(r'''
███████╗██╗░░░░░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░░░░░░░██████╗░░█████╗░██████╗░███████╗██╗
██╔════╝██║░░░░░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔══██╗╚════██║██║
█████╗░░██║░░░░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║█████╗██████╦╝██║░░██║██████╔╝░░███╔═╝██║
██╔══╝░░██║░░░░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║╚════╝██╔══██╗██║░░██║██╔══██╗██╔══╝░░██║
███████╗███████╗███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝░░░░░░██████╦╝╚█████╔╝██║░░██║███████╗██║
╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝                                   \/       
''')

if __name__ == "__main__":
    main()
