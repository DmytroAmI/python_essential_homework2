class Editor:
    @staticmethod
    def view_document():
        print("View document")

    def edit_document(self):
        print("Editing is not available for the free version!")


class ProEditor(Editor):

    KEY = "QWE123QWE"

    def edit_document(self):
        print("Welcome to the document editor!")


if __name__ == "__main__":

    if ProEditor.KEY == input("Enter licence code for editor: "):
        editor = ProEditor()
    else:
        editor = Editor()

    editor.view_document()
    editor.edit_document()
