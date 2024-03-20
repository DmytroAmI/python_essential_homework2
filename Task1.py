class Editor:
    """Describe a free file editor"""
    @staticmethod
    def view_document():
        """Open and show a document"""
        print("View document")

    def edit_document(self):
        """Edit a document, not available in this version"""
        print("Editing is not available for the free version!")


class ProEditor(Editor):
    """Describe a pro file editor"""

    KEY = "QWE123QWE"

    def edit_document(self):
        """Edit a document"""
        print("Welcome to the document editor!")


if __name__ == "__main__":

    if ProEditor.KEY == input("Enter licence code for editor: "):
        editor = ProEditor()
    else:
        editor = Editor()

    editor.view_document()
    editor.edit_document()
