import requests


# Fetch API data
def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch API data")
        return []


# Display all users
def display_users(users):
    print("\n===== USER DETAILS =====")

    for user in users:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("------------------------")


# Search user by name
def search_user(users):
    keyword = input("\nEnter name to search: ")

    print("\n===== SEARCH RESULT =====")

    found = False

    for user in users:
        if keyword.lower() in user["name"].lower():
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            found = True

    if not found:
        print("No matching user found")


# Filter users by city
def filter_city(users):
    city = input("\nEnter city to filter: ")

    print("\n===== FILTER RESULT =====")

    found = False

    for user in users:
        if city.lower() == user["address"]["city"].lower():
            print("Name:", user["name"])
            print("Email:", user["email"])
            found = True

    if not found:
        print("No users found in this city")


# Main Program
def main():

    print("Fetching API Data...")

    users = fetch_users()

    if users:
        display_users(users)

        search_user(users)

        filter_city(users)

    else:
        print("No data available")


if __name__ == "__main__":
    main()