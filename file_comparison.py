import difflib

def compare_files(file1, file2):
    # Open file for reading in text mode (default mode)
    with open(file1) as f1, open(file2) as f2:
        # Read the lines of each file
        f1_text = f1.readlines()
        f2_text = f2.readlines()
        
        # Create a Differ object
        differ = difflib.Differ()

        # Compare the two files
        diffs = list(differ.compare(f1_text, f2_text))

        # Print the differences
        for diff in diffs:
            print(diff)

# Test the function
compare_files('file1.txt', 'file2.txt')
