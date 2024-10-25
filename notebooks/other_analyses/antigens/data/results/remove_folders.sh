# Loop through all directories in the current path
for folder in */*/; do
    # Extract the folder name (like P09382)
    folder_name=$(basename "$folder")

    # Check if the folder contains a subfolder with the same name
    if [ -d "$folder/$folder_name" ]; then
        # Move the contents of the redundant subfolder to the parent
        mv "$folder/$folder_name/"* "$folder"

        # Remove the redundant subfolder
        rmdir "$folder/$folder_name"
        echo "Removed redundant folder: $folder/$folder_name"
    fi
done
