def search(file_path):
    print("Searching...")

    sections = ""
    books = "Books:\n"

    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line

    print("Done!")

    return f"{sections}\n\n{books}"

def save(file_path)