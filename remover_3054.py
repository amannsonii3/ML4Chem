import os
import re
import argparse

def extract_indices(text_file_path):
    """
    Extracts molecule indices from a given text file.

    Parameters:
    - text_file_path (str): Path to the text file containing molecule indices.

    Returns:
    - indices (list of int): List of extracted molecule indices.
    """
    indices = []
    # Regular expression to match lines starting with an integer index
    index_pattern = re.compile(r'^(\d+)\s+')

    with open(text_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            match = index_pattern.match(line)
            if match:
                index = int(match.group(1))
                indices.append(index)
    
    return indices

def remove_xyz_files(indices, xyz_dir):
    """
    Removes XYZ files corresponding to the given indices from the specified directory.

    Parameters:
    - indices (list of int): List of molecule indices.
    - xyz_dir (str): Path to the directory containing XYZ files.
    """
    removed_files = []
    not_found_files = []
    error_files = []

    for index in indices:
        # Format the index to a 6-digit zero-padded string
        index_str = f"{index:06d}"
        filename = f"dsgdb9nsd_{index_str}.xyz"
        filepath = os.path.join(xyz_dir, filename)
        
        if os.path.isfile(filepath):
            try:
                os.remove(filepath)
                removed_files.append(filename)
                print(f"Removed: {filename}")
            except Exception as e:
                error_files.append((filename, str(e)))
                print(f"Error removing {filename}: {e}")
        else:
            not_found_files.append(filename)
            print(f"File not found: {filename}")

    # Summary
    print("\n=== Summary ===")
    print(f"Total files attempted to remove: {len(indices)}")
    print(f"Successfully removed: {len(removed_files)}")
    print(f"Files not found: {len(not_found_files)}")
    print(f"Files failed to remove due to errors: {len(error_files)}")
    
    if error_files:
        print("\nFiles that encountered errors during removal:")
        for fname, error in error_files:
            print(f"{fname}: {error}")

def main():
    """
    Main function to execute the extraction and removal process.
    """
    # Set up argument parsing for flexibility
    parser = argparse.ArgumentParser(description="Remove XYZ files based on indices from a text file.")
    parser.add_argument(
        '--text_file',
        type=str,
        required=True,
        help='Path to the text file containing molecule indices.'
    )
    parser.add_argument(
        '--xyz_dir',
        type=str,
        required=True,
        help='Path to the directory containing XYZ files.'
    )
    
    args = parser.parse_args()
    
    text_file_path = args.text_file
    xyz_dir = args.xyz_dir

    # Validate input paths
    if not os.path.isfile(text_file_path):
        print(f"Error: The text file '{text_file_path}' does not exist.")
        return
    
    if not os.path.isdir(xyz_dir):
        print(f"Error: The directory '{xyz_dir}' does not exist.")
        return

    # Extract indices
    print(f"Extracting indices from '{text_file_path}'...")
    indices = extract_indices(text_file_path)
    print(f"Total indices extracted: {len(indices)}")

    if not indices:
        print("No valid indices found. Exiting.")
        return

    # Confirm before deletion
    confirmation = input(f"Proceed to remove {len(indices)} XYZ files from '{xyz_dir}'? (y/n): ").lower()
    if confirmation != 'y':
        print("Operation cancelled by the user.")
        return

    # Remove XYZ files
    print(f"\nRemoving XYZ files from '{xyz_dir}'...")
    remove_xyz_files(indices, xyz_dir)
    print("Operation completed.")

if __name__ == "__main__":
    main()

