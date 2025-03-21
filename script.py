import time
import sys
import os

# Hide the cursor (works on most terminals)
print("\033[?25l", end='', flush=True)

def print_lyrics():
    # Lyrics with durations (keeping your perfect sync)
    lines = [
        ("So I'ma love you every night like it's the last night", 3.5),
        ("Like it's the last night", 1.5),
        ("If the world was ending", 1.8),
        ("I'd wanna be next to you", 2.2),
        ("If the party was over", 1.9),
        ("And our time on Earth was through", 2.5),
        ("I'd wanna hold you just for a while", 2.8),
        ("And die with a smile", 1.7),
        ("If the world was ending", 1.8),
        ("I'd wanna be next to you", 3.5),
        ("Right next to you", 2.5),
    ]
    delays = [0.6, 0.7, 1.0, 4.6, 1.0, 3.6, 1.7, 2.0, 1.2, 1.7, 0.5]

    for i, (line, line_duration) in enumerate(lines):
        char_delay = line_duration / len(line)
        start_time = time.time()  # Track start time for this line

        for j, char in enumerate(line):
            # Calculate when this character *should* appear
            target_time = start_time + (j * char_delay)
            while time.time() < target_time:
                pass  # Wait precisely until the target time
            print(char, end='', flush=True)

        # Precise delay between lines
        time.sleep(delays[i])
        print('')  # Newline

# Run the function
print_lyrics()

# Show the cursor again when done (optional)
print("\033[?25h", end='', flush=True)