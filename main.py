import time

def fast_tap_game():
    print("=== Welcome to the Riaku Fast Tap Challenge! ===")
    print("Tap ENTER as fast as you can in 5 seconds!")
    print("Ready... GO!")

    start_time = time.time()
    taps = 0

    while time.time() - start_time < 5:
        input()  # Waits for you to press ENTER
        taps += 1

    print("\n--- Time's up! ---")
    print(f"You made {taps} taps.")
    print("Each tap earns you 10 Riaku Points!")
    print(f"Total Riaku Points: {taps * 10}")

# Run the game when you execute this file
if __name__ == "__main__":
    fast_tap_game() 