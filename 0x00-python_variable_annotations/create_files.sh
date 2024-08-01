#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <number_of_files> <base_filename>"
    exit 1
fi

# Get the number of files to create and the base filename
num_files="$1"
base_name="${2%.*}"
extension="${2##*.}"

# Validate that num_files is a non-negative integer
if ! [[ "$num_files" =~ ^[0-9]+$ ]]; then
    echo "Error: <number_of_files> must be a non-negative integer."
    exit 1
fi

# Loop to create the specified number of files
for ((i=0; i<=num_files; i++)); do
    # Construct the file name
    file_name="${i}-${base_name}.${extension}"
    
    # Create the file
    touch "$file_name"
    
    # Optional: Display a message for each file created
    echo "Created file: $file_name"
done

