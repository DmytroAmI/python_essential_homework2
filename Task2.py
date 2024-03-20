class Rectangle:
    """Describe parent class Rectangle"""
    def __init__(self, length, width):
        """Initialize the Rectangle attributes"""
        self.length = length
        self.width = width

    def __str__(self):
        """Return a string representation of the attributes"""
        return f"length: {self.length}, width: {self.width}"


class Button(Rectangle):
    """Describe child class Button"""
    def __init__(self, length, width, text, font):
        """Initialize the attributes"""
        super().__init__(length, width)
        self.font = font
        self.text = text

    def __str__(self):
        """Return a string representation of the attributes"""
        return super().__str__() + f", text: {self.text}, font: {self.font}"

    @staticmethod
    def press_the_button():
        """Click on the button"""
        return "Click"


if __name__ == "__main__":
    rectangle = Rectangle(10, 15)
    print(rectangle)

    button = Button(10, 15, "Press", "Arial")
    print(button)
    print(button.press_the_button())
