from vault import unlock_data

def main():
    # Ask for the password
    password = input("Enter your password: ")
    
    # Read and decrypt the clipboard history
    try:
        with open("vault/secret.txt", "rb") as f:
            print("\n📋 Clipboard History:")
            for i, line in enumerate(f, 1):
                decrypted = unlock_data(line.strip(), password)
                print(f"{i}. {decrypted}")
    except FileNotFoundError:
        print("No clipboard history found!")

if __name__ == "__main__":
    main()