from core.start_protection import protect_file

path = input("Enter file path: ")

success = protect_file(path)

if success:
    print("Protection started successfully.")
else:
    print("Failed to protect file.")
    
