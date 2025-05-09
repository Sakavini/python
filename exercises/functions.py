import os
import time

def welcome():
    print("=== Welcome to the calculator Python ===")
    print("Select one option to start:")
    print()
    print("1 - Start calculator")
    print("2 - Exit calculator")
    print()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def countdown(seconds):
    for i in range(seconds, 0, -1): # Start in the seconds, end in 0 and the -1 decreases in each step
        print(f"{i} segundo(s)...")
        time.sleep(1) # Pause 1 second in each iteration of loop