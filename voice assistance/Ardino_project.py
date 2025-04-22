import serial
import time

# Connect to the correct COM port
arduino = serial.Serial('COM6', 9600,)
time.sleep(2)  # Wait for Arduino to reset

# Function to send command with delay
def send_command(cmd, wait=5):
    print(f"Sending '{cmd}'...")
    arduino.write(cmd.encode())  # Send the character
    time.sleep(wait)  # Wait for Arduino to complete action
    #arduino.close()

"""commands = [('R', 5),
    ('h', 6),  # hi
    ('H', 7),  # hands up
    ('l', 3),  # look left
    ('u', 7),  # upper cut
    ('s', 8),
    ('w', 8),
    ('n', 4),
    ('d', 8),
    ('p', 4),
    ('r', 3),
    ('S', 6),# smash   # look left (duplicate for testing)
]"""

# Send all commands one by one
"""for cmd, delay_time in commands:"""
#send_command('h')
"""arduino.close()
print("All commands sent. Connection closed.")"""