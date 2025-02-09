import serial
import time
import cv2
import numpy as np



# Load the image in grayscale

image = cv2.imread("F:/.IITM HACKATHON/preprocessing/Normal-1.png", cv2.IMREAD_GRAYSCALE)

# Resize the image to 8x12 to get 96 elements (8*12 = 96)
resized_image = cv2.resize(image, (12, 8))

# Normalize the image (scale pixel values to range [0, 1])
normalized_image = resized_image / 255.0

# Flatten the image into a 1D array of 96 elements
input_array = normalized_image.flatten()

# Convert to float32 type for compatibility with C program
input_array = input_array.astype(np.float32)

# ... (Your existing code to generate input_array) ...

# Reshape the array to have 7 columns (7 data elements per line)
num_rows = len(input_array) // 7  # Calculate the number of full rows
reshaped_array = input_array[:num_rows * 7].reshape(1, 91) # Reshape only the elements that fit completely

float_array = reshaped_array.flatten().tolist()

# Print the reshaped array
#for row in reshaped_array:
#  print(', '.join([f'{x:.18f}' for x in row]))


# Open serial connection
ser = serial.Serial('COM7', 115200)  # Increased baud rate for faster transmission

try:
    # Wait for the board to initialize
    time.sleep(2)

    # Read and print any initial messages from the board
    while ser.in_waiting:
        print(ser.readline().decode().strip())

    # Send start marker
    print("Sending start...")
    #ser.write(b"Start\n")
    time.sleep(0.1)

    # Send float array
    #print("Sending float array...")
    for value in float_array:
        # Convert float to string with 2 decimal places and add a newline
        #formatted_values = [f"{x:.19f}" for x in value]
    # Join the formatted values with commas
        data_string = f"{value:.19f}\n"
        
        ser.write(data_string.encode())
        #print(f"Sent: {data_string.strip()}")
        time.sleep(0.01)  # Small delay to ensure data is sent

    # Send end marker
    print("Sending end...")
    #ser.write(b"End\n")

    # Wait and print the response from the board
    time.sleep(0.5)
    while ser.in_waiting:
        print(ser.readline().decode().strip())

finally:
    ser.close()
    #print("Serial connection closed.")

import serial
from time import sleep

ser = serial.Serial("COM7", 115200)
try:
 def receive_data(ser):
    response = ""
    while True:
        #if ser.any():  # Check if data is available
            data = ser.read()  # Read data
            if data:  # Ensure data is not None
                try:
                    data = data.decode('utf-8')  # Decode without keyword arguments
                except:
                    data = ""  # Handle decoding errors by setting data as empty
                response += data
                #print("Received:", data)  # Debugging output
                if '\n' in data:  # Break if a newline is received
                    break
 
    response = response.strip()  # Remove extra whitespace and newlines
    return response

#while True:
#    print(receive_data(ser))
#    sleep(0.1)

 filename = f"test_result1.txt"
 with open(filename, 'w') as file:
    print(f"Writing data to {filename}")
    while True:
        received_data = receive_data(ser)
        print(received_data)  # Print to console
        file.write(received_data + '\n')  # Write to file
        file.flush()  # Ensure data is written immediately
        if received_data == "============================":
         break  # Stop if "END" is received
        sleep(0.1)

 print(f"Data collection complete. Data saved to {filename}")
finally:
  
    ser.close()
    print("Serial connection closed.")
