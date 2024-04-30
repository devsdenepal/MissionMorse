from modules import arduino_send
#arduino_send(command)
import tkinter as tk

class TextSectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Section App")
        
        self.sections = [
            "This is section 1. Please read this carefully.",
            "This is section 2. Please read this carefully.",
            "This is section 3. Please read this carefully."
        ]
        self.current_section_index = 0
        
        self.section_label = tk.Label(master, text=self.sections[self.current_section_index], wraplength=300)
        self.section_label.pack(pady=20)
        
        self.next_button = tk.Button(master, text="Next", command=self.show_next_section)
        self.next_button.pack()
        
    def show_next_section(self):
        self.current_section_index += 1
        if self.current_section_index < len(self.sections):
            self.section_label.config(text=self.sections[self.current_section_index])
        else:
            self.section_label.config(text="End of sections reached.")
            self.next_button.config(state=tk.DISABLED)
        # Call the function that requires user input
        self.user_input_function()

    def user_input_function(self):
        # This is just a placeholder function for demonstration purposes
        # You should replace this with your actual function that requires user input
        user_input = tk.simpledialog.askstring("User Input", "Enter some input:")
        if user_input:
            print("User input:", user_input)

def main():
    root = tk.Tk()
    app = TextSectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
