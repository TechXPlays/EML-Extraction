import os
import argparse

def delete_files_by_size(folder_path='.', size_bytes=4096):
    try:
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path) and os.path.getsize(file_path) == size_bytes:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
        print("Deletion complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete files of a specific size in a folder and its subdirectories.")
    parser.add_argument("--size", type=int, required=True, help="Size of files to delete in bytes")

    args = parser.parse_args()
    delete_files_by_size(size_bytes=args.size)
