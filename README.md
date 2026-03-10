# dublicate_detection
Approach / Algorithm

Steps

Read the file line by line (so we don't load everything into memory).

Maintain a Hash Set to store seen email addresses.

Maintain another Set/List for duplicates.

For each email:

If the email is not in the hash set, add it.

If the email already exists in the set, add it to the duplicates list.

Continue until the file is fully processed.

Output the list of duplicate emails.

Data Structures Used
1️⃣ Hash Set

Used to store already seen email addresses.

Reason:

Very fast lookup

Average lookup time O(1)

2️⃣ Set/List for duplicates

Used to store emails that appear more than once.

Python Example Implementation
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
    
Time Complexity

We scan the file once.

O(n)

Where n = number of emails (100 million).

Space Complexity

We store emails in a hash set.

O(n)
