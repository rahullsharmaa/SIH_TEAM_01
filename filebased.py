
import os

file_path = 'queries.txt'

def add_query_to_file(query_id, query_text):
    with open(file_path, 'a') as file:
        file.write(f"{query_id}:{query_text}\n")
    print(f"Query with ID {query_id} added to file.")

def view_queries_from_file():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
            if content:
                for line in content:
                    query_id, query_text = line.strip().split(':')
                    print(f"Query ID: {query_id}, Query: {query_text}")
            else:
                print("No queries found in file.")
    else:
        print("File not found.")

def delete_query_from_file(query_id):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            found = False
            for line in lines:
                if not line.startswith(query_id):
                    file.write(line)
                else:
                    found = True

            if found:
                print(f"Query with ID {query_id} has been deleted from file.")
            else:
                print(f"Query with ID {query_id} not found.")
    else:
        print("File not found.")

while True:
    print("\nOptions: 1. Add Query 2. View Queries 3. Delete Query 4. Exit")
    choice = input("Enter your num: ")

    if choice == '1':
        query_id = input("Enter Query ID: ")
        query_text = input("Enter Query: ")
        add_query_to_file(query_id, query_text)

    elif choice == '2':
        view_queries_from_file()

    elif choice == '3':
        query_id = input("Enter Query ID to delete: ")
        delete_query_from_file(query_id)

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, try again.")
