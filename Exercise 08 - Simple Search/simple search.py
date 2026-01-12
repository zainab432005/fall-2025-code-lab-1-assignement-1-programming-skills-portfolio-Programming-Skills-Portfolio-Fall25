names = ["amal", "baraa", "salma", "leen", "akram", "omer"]
search_term = input("Enter the name to search for: ").strip()
if search_term in names:
    print(f"{search_term} found in the list!")
else:
    print(f"{search_term} not found in the list.")
