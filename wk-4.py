# File handling

input_file = 'input.txt'
output_file = 'output.txt'

file =  open(input_file, 'w') 
content = file.write("This is a text content \n")

file =  open(input_file, 'r') 
content = file.read()

new_content = content.upper()

file = open(output_file, 'w') 
file.write(new_content)

print('Done! The new file has been created.')

# Error handling with try-except 
try:
     file_name = input("Enter the filename:")
     with open(file_name, "r") as file:
        data = file.read();
except FileNotFoundError:
    print("File not found. Please check the filename.")
 