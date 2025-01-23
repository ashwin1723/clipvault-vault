import time
import pyperclip
from vault import lock_data

def watch_clipboard(password: str):
    last_text = ""
    while True:
        current_text = pyperclip.paste()
        
        if current_text != last_text:
            print("New copied text detected!")
            encrypted = lock_data(current_text, password)
            
            # Save to local vault
            with open("vault/secret.txt", "ab") as f:
                f.write(encrypted + b"\n")
            
            last_text = current_text
        
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    password = input("Enter your password: ")
    watch_clipboard(password)