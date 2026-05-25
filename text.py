import time
import os
import math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 3D-style ASCII frames for hand signs (1, 2, 3)
frames = [
    # Frame 1: Number 1 (Index finger up)
    """
    ╔═══════╗
   ╔╝       ╚╗
   ║    ☻    ║  🤖
   ║   /|\\   ║
   ║    |    ║  ← NUMBER 1
   ╚═══════╝
        ║
       / \\
    """,
    
    # Frame 2: Number 2 (Index + Middle up)
    """
    ╔═══════╗
   ╔╝       ╚╗
   ║    ☻    ║  🤖
   ║  //|\\\\  ║
   ║   / |    ║  ← NUMBER 2
   ╚═══════╝
        ║
       / \\
    """,
    
    # Frame 3: Number 3 (Index + Middle + Ring up)
    """
    ╔═══════╗
   ╔╝       ╚╗
   ║    ☻    ║  🤖
   ║ ///|\\\\ ║
   ║  // |   ║  ← NUMBER 3
   ╚═══════╝
        ║
       / \\
    """,
    
    # Bonus: Wave (all fingers)
    """
    ╔═══════╗
   ╔╝ ✨✨ ✨ ╚╗
   ║    ☻    ║  🤖
   ║ ////|\\\\ ║
   ║  /// |  ║  ← WAVE!
   ╚═══════╝
        ║
       / \\
    """
]

def animate_3d_handsigns(loops=3, delay=0.8):
    for loop in range(loops):
        print(f"\n🎬  LOOP {loop+1}/{loops} - 3D Robot Hand Signs  🎬\n")
        for i, frame in enumerate(frames):
            clear_screen()
            print("═" * 50)
            print("     3D ROBOT HAND SIGN ANIMATION")
            print("═" * 50)
            print(frame)
            print("═" * 50)
            print("Use mouse to interact in VPython version!")
            print("═" * 50)
            time.sleep(delay)
    
    print("\n✨ Animation Complete! Install vpython for 3D version ✨")

# Rotating 3D effect bonus frames
def bonus_rotate_effect():
    angles = ['/', '|', '\\', '|']
    for _ in range(3):
        for angle in angles:
            clear_screen()
            print(f"🔄 ROTATING 3D ROBOT ({angle})")
            print("""
              _____
             /     \\
            |  ☻  |  🤖
             \\___/
              /|\\
             / | \\
            """)
            time.sleep(0.2)

if __name__ == "__main__":
    print("🚀 Starting 3D Text Robot Hand Sign Animation...")
    time.sleep(1)
    bonus_rotate_effect()
    animate_3d_handsigns(loops=4, delay=0.7)