import tkinter as tk #importing the built in tkinter module.

LARGE_FONT_STYLE = ("Arial", 40, "bold") #defining a constant for large font style.
SMALL_FONT_STYLE = ("Arial", 16) #defining a constant for small font style.
DIGITS_FONT_STYLE = ("Arial", 24, "bold") #defining a constant for digits font style.
DEFAULT_FONT_STYLE = ("Arial", 20) #defining a constant for default font style.

OFF_WHITE = "#F8FAFF" #defining color off_white.
WHITE = "#FFFFFF" #defining color white.
LIGHT_BLUE = "#765898" #defining color light_blue.
LIGHT_GRAY = "#F5F5F5" #defining color light_gray.
LABEL_COLOR = "#25265E" #defining label_color.


class Calculator: #creating a class to store all the components and functions.
    def __init__(self): #creating an init method for our class for all the initializations.
        self.window = tk.Tk() #creating the main window usking the tk class of the tkinter module.
        self.window.geometry("375x667") #specifying the width and the height of this window.
        self.window.resizable(0,0) #disabling resizing for this window.
        self.window.title("Calculator") #giving a name to be displayed in the title bar of this window.

        self.total_expression = "" #defnining total expression for the label.
        self.current_expression = "" #defining current expression for the label.
        self.display_frame = self.create_display_frame() #creating a frame for the display.

        self.total_label, self.label = self.create_display_labels() #creating display labels.

        self.digits = { #specifying the location of the digits as the buttons for the calculator.
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} #specifying a dicitonary for the arithmetic operators in python.
        self.buttons_frame = self.create_buttons_frame() #creating a frame for the buttons.

        self.buttons_frame.rowconfigure(0, weight=1) #formatting the frame for the buttons.
        for x in range(1, 5): #using for loop to expand the buttons to fill in empty spaces.
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons() #calling the digit buttons.
        self.create_operator_buttons() #calling the operator buttons.
        self.create_special_buttons() #calling the special buttons.
        self.bind_keys()

    def bind_keys(self): #defining a method for binding keys to calculator.
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self): #defining a method for the special buttons.
        self.create_clear_button() #calling the clear button.
        self.create_equals_button() #calling the equals to button.
        self.create_square_button() #calling the square button.
        self.create_sqrt_button() #calling the square root button.

    def create_display_labels(self): #defining a method for the display label.
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE) #formatting the total display label.
        total_label.pack(expand=True, fill='both') #packing the total display label.

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE) #formatting the display label.
        label.pack(expand=True, fill='both') #packing the display label.

        return total_label, label #returning the label.

    def create_display_frame(self): #defining a method for the display frame.
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY) #specifying shape,height and color of the frame.
        frame.pack(expand=True, fill="both") #packing this frame to the main window.
        return frame #returning the frame.

    def add_to_expression(self, value): #defining a method to take a value and work on an expression.
        self.current_expression += str(value) #appending a value to an expression.
        self.update_label() #updating this current expression.

    def create_digit_buttons(self): #defining a method for creating the buttons for the digits on the calculator.
        for digit, grid_value in self.digits.items(): #using for loop to go through our dictionary of buttons for the calculator.
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=1, command=lambda x=digit: self.add_to_expression(x)) #formatting the button for digits on the calculator.
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) #specifying the buttons to be ordered in a grid with a specified number of rows and columns.

    def append_operator(self, operator): #
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self): #creating a method for operator buttons.
        i = 0 #defining a counter variable
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=1, command=lambda x=operator: self.append_operator(x)) #formatting the operator buttons.
            button.grid(row=i, column=4, sticky=tk.NSEW) #placing the buttons in the grid.
            i += 1 #increasing the value of i by 1

    def clear(self): #defining a method to clear the current and the total expression
        self.current_expression = "" #empty string
        self.total_expression = "" #empty string
        self.update_label()
        self.update_total_label()

    def create_clear_button(self): #creating a method for clear button.
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=1, command=self.clear) #formatting the clear button.
        button.grid(row=0, column=1, sticky=tk.NSEW) #placing the button in the grid.

    def square(self): #
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self): #defining a method for the square button.
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=1, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self): #
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self): #defining a method for the square root button.
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=1, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self): #defining an evaluate method
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = "" #reset the expression.
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self): #creating a method for equals to button.
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=1, command=self.evaluate) #formatting the equals to button.
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW) #placing the equals to button in a grid.

    def create_buttons_frame(self): #defining a method for the buttons frame.
        frame = tk.Frame(self.window) #creating a frame for the buttons.
        frame.pack(expand=True, fill="both") #packing the frame.
        return frame #returning the frame.

    def update_total_label(self): #defining a method for updating the total label.
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression) #updating the value of the total label to the value of the expression.

    def update_label(self): #defining a method for updating the display label.
        self.label.config(text=self.current_expression[:11]) #limiting the result to 11 digits.

    def run(self): #creating a method to start the window.
        self.window.mainloop() #specifies the window to be run until it is closed.

if __name__ == "__main__": #allows the code to be executed when the file is run as script.
    calc = Calculator() #creating an object of our class.
    calc.run() #running the object.


