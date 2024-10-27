import time
import random

def create_rocket():
    return [
        "   /\\   ",
        "  /  \\  ",
        " /____\\ ",
        " |    | ",
        " |    | ",
        " |____| ",
        "/      \\",
        "--------"
    ]

def launch_rocket():
    rocket = create_rocket()
    height = 0

    print("Prepare for launch!")
    for countdown in range(5, 0, -1):
        print(f"T-minus {countdown}...")
        time.sleep(1)

    print("Liftoff!")
    
    while height < 15:
        print("\n" * (20 - height))
        print("\n".join(rocket))
        print("\n" * height)
        print("=" * 20)
        
        height += 1
        time.sleep(0.2)
        
        if height > 5:
            rocket.append(" " * random.randint(0, 5) + "*" * random.randint(1, 3))

    print("The rocket has reached orbit!")

if __name__ == "__main__":
    launch_rocket()
