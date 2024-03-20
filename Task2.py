class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"length: {self.length}, width: {self.width}"


class Button(Rectangle):
    def __init__(self, length, width, text, font):
        super().__init__(length, width)
        self.font = font
        self.text = text

    def __str__(self):
        return super().__str__() + f", text: {self.text}, font: {self.font}"

    @staticmethod
    def press_the_button():
        print("Click")


if __name__ == "__main__":
    rectangle = Rectangle(10, 15)
    print(rectangle)

    button = Button(10, 15, text="Press", font="Arial")
    print(button)
    button.press_the_button()
