import customtkinter as ctk
import google.generativeai as genai

# Configure the appearance of the CustomTkinter app
ctk.set_appearance_mode("Dark")  # Options: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

class ChatBotApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App window configuration
        self.title("Gemini Chatbot")
        self.geometry("900x600")
        self.resizable(True, True)

        # Chat display (output area)
        self.chat_display = ctk.CTkTextbox(self, height=400, wrap="word", font=("Arial", 12))
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
        self.chat_display.configure(state="disabled")  # Initialize as disabled

        # User input field
        self.user_input = ctk.CTkEntry(self, placeholder_text="Type your message here...", font=("Arial", 14))
        self.user_input.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

        # Send button
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=(5, 10))

        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Configure Gemini API
        self.configure_gemini_api()

    def configure_gemini_api(self):
        """
        Configures the Gemini API with the appropriate API key.
        """
        try:
            genai.configure(api_key="AIzaSyCV7sjVrr1B3xKLo56-SUq3sDrV4wkHLEg")  # Replace with your actual API key
        except Exception as e:
            self.append_chat(f"Error configuring API: {e}\n")

    def send_message(self):
        # Get user input
        user_message = self.user_input.get()
        if user_message.strip():
            self.append_chat(f"You: {user_message}\n")
            self.user_input.delete(0, ctk.END)

            # Call Gemini API
            try:
                bot_response = self.get_gemini_response(user_message)
                self.append_chat(f"Bot: {bot_response}\n")
            except Exception as e:
                self.append_chat(f"Error: {str(e)}\n")

    def append_chat(self, message):
        """
        Appends messages to the chat display.
        """
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", message)
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")

    def get_gemini_response(self, user_message):
        """
        Calls the Gemini API with the user's message and retrieves the response.
        """
        try:
            response = genai.GenerativeModel(
                "gemini-1.5-flash"
            )
            message = response.generate_content(user_message)
            return message.text

            return response.GenerativeModel("gemini-1.5-flash")
        except Exception as e:
            raise Exception(f"Failed to get response from Gemini API: {str(e)}")

if __name__ == "__main__":
    app = ChatBotApp()
    app.mainloop()
