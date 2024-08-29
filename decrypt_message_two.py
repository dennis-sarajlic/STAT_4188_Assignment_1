encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

# Create a list to edit from the string
decrypted_message = list(encrypted_message)

# Set initial positions
i, j = 1, len(encrypted_message) - 2

# Iterate through the message 
while i <= j:
    decrypted_message[i], decrypted_message[j] = decrypted_message[j], decrypted_message[i]
    i += 2
    j -= 2

print("".join(decrypted_message))