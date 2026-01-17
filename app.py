
notes=[]
def add_note(note):
    notes.append(note)
def get_notes():
    return notes
print("Note-taking app is running.")
def rename_note(note):
    if note in notes:
        new_name = input("Enter the new name for the note: ")
        index = notes.index(note)
        notes[index] = new_name
        print(f"Note renamed to: {new_name}")
    else:
        print("Note not found.")
def delete_note(note):
            if note in notes:
                notes.remove(note)
                print(f"Note '{note}' deleted.")
            else:
                print("Note not found.")

