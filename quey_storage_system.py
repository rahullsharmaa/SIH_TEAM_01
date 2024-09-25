
queries = {}

def add_query(query_id, query_text):
    queries[query_id] = query_text
    print(f"Query with Id {query_id} has been added.")

def view_queries():
    if queries:
        for query_id, query_text in queries.items():
            print(f"Query ID: {query_id}, Query: {query_text}")
    else:
        print("No quirie available.")

def delete_query(query_id):
    try:
        del queries[query_id]
        print(f"Query with ID {query_id} has been delete.")
    except KeyError:
        print(f"Query ID {query_id} not found.")

# Main program loop
while True:
    print("\nOptions: 1. Add Query 2. View Queries 3. Delete Query 4. Exit")
    choice = input("Enter your num: ")

    if choice == '1':
        query_id = input("Enter Query ID: ")
        query_text = input("Enter Query: ")
        add_query(query_id, query_text)

    elif choice == '2':
        view_queries()

    elif choice == '3':
        query_id = input("Enter Query ID to delete: ")
        delete_query(query_id)

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, try again.")
