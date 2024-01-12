#!/bin/bash

# Set the source and destination directories
source_directory="Excel"
destination_directory="backup"

# Create a timestamp for the backup folder
backup_timestamp=$(date +"%Y%m%d_%H%M%S")

# Create a backup by copying and replacing the entire folder
rsync -av "$source_directory/" "$destination_directory/backup_$backup_timestamp/"

echo "Backup completed at $(date)"
