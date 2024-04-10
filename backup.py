import os
import pandas as pd
import sqlite3

def backup_excel_to_sql(excel_file, conn):
    try:
        # Read Excel data into a DataFrame
        df = pd.read_excel(excel_file)

        # Extract table name from file name (assuming file name without extension)
        table_name = os.path.splitext(os.path.basename(excel_file))[0]

        # Insert DataFrame into SQLite table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Backup completed for {excel_file}")
    except Exception as e:
        print(f"Error backing up {excel_file}: {e}")

def backup_folder_to_sql(folder_path, conn):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xlsx'):  # Assuming all Excel files have .xlsx extension
                excel_file = os.path.join(root, file)
                backup_excel_to_sql(excel_file, conn)

if __name__ == "__main__":
    # Set up SQLite connection and cursor
    db_file = 'backup.db'  # SQLite database file
    conn = sqlite3.connect(db_file)

    # Set the source directory
    source_directory = "Excel"  # Change to your source directory

    # Create tables for each Excel file and backup data
    backup_folder_to_sql(source_directory, conn)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("All backups completed successfully")
