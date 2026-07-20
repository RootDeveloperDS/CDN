import os

# Folders to ignore
IGNORE = {
    ".git",
    ".vs",
    ".vscode",
}

def tree(path, prefix="", output=None):
    items = sorted(os.listdir(path))

    # Remove ignored folders
    items = [i for i in items if i not in IGNORE]

    for index, item in enumerate(items):
        full_path = os.path.join(path, item)

        connector = "└── " if index == len(items) - 1 else "├── "
        line = prefix + connector + item

        print(line)
        output.write(line + "\n")

        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if index == len(items) - 1 else "│   ")
            tree(full_path, new_prefix, output)


root = os.getcwd()

with open("folder_structure.txt", "w", encoding="utf-8") as output:
    output.write(os.path.basename(root) + "\n")
    print(os.path.basename(root))
    tree(root, output=output)

print("\n✔ Folder structure saved to folder_structure.txt")