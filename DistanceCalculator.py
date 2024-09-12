import numpy as np
import tkinter as tk
from tkinter import messagebox

# Function to calculate distances
def distances_option_calculator(X, y, distance_type):
    if X is None or y is None or distance_type is None:
        raise ValueError("All arguments (X, y, distance_type) are required.")
    
    X = np.array(X)
    y = np.array(y)
    
    if distance_type == 'euclidian':
        return np.sqrt(np.sum((X - y) ** 2))
    elif distance_type == 'manhattan':
        return np.sum(np.abs(X - y))
    elif distance_type == 'hamming':
        return np.sum(X != y)
    else:
        raise ValueError("Invalid distance type. Choose from 'euclidian', 'manhattan', 'hamming'.")

# Function to get input and calculate the result
def calculate_distance():
    try:
        # Get X and y from input fields
        X = list(map(int, entry_x.get().split(",")))
        y = list(map(int, entry_y.get().split(",")))
        
        # Get selected distance type
        distance_type = distance_var.get().lower()
        
        # Calculate the distance
        result = distances_option_calculator(X, y, distance_type)
        
        # Display the result in a message box
        messagebox.showinfo("Result", f"The calculated {distance_type} distance is: {result}")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main application window
root = tk.Tk()
root.title("Distance Calculator")

# Set the window size
root.geometry("400x300")

# Create and place labels and input fields
label_x = tk.Label(root, text="Enter X (comma-separated):")
label_x.pack(pady=5)
entry_x = tk.Entry(root)
entry_x.pack(pady=5)

label_y = tk.Label(root, text="Enter Y (comma-separated):")
label_y.pack(pady=5)
entry_y = tk.Entry(root)
entry_y.pack(pady=5)

label_distance_type = tk.Label(root, text="Choose distance type:")
label_distance_type.pack(pady=5)

# Variable to store the selected distance type
distance_var = tk.StringVar(value="euclidian")

# Create radio buttons for selecting the distance type
radio_euclidean = tk.Radiobutton(root, text="Euclidean", variable=distance_var, value="euclidian")
radio_euclidean.pack(anchor='w')
radio_manhattan = tk.Radiobutton(root, text="Manhattan", variable=distance_var, value="manhattan")
radio_manhattan.pack(anchor='w')
radio_hamming = tk.Radiobutton(root, text="Hamming", variable=distance_var, value="hamming")
radio_hamming.pack(anchor='w')

# Create a button to trigger the distance calculation
button_calculate = tk.Button(root, text="Calculate Distance", command=calculate_distance)
button_calculate.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()