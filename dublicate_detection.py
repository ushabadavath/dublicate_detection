def find_duplicates(file_path):
    seen = set()
    duplicates = set()

    with open(file_path, "r") as file:
        for line in file:
            email = line.strip()

            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates


duplicates = find_duplicates("emails.txt")

for email in duplicates:
    print(email)