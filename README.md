# HexStresser

HexStresser is a high-performance UDP flood tool designed to stress-test servers by sending UDP packets to a target IP and port. It supports up to 15,000 concurrent threads, simulating a flood of UDP packets to test a server's resilience.

## Features

- **Multi-threading support** for up to 15,000 concurrent threads.
- **Randomized packet generation** using `random._urandom()` for more realistic attack simulations.
- **Colored output** with real-time feedback on the attack status.
- **Customizable settings** including target IP, port, packet size, and thread count.
- **Dynamic progress display** showing the current thread count in "K" format (e.g., 1K, 10K).
  
![alt text](https://giphy.com/gifs/cyberwar-3oEjHQxSq1ZSBXZgeQ)

## Requirements

- Python 3.x
- No external libraries required (uses only built-in Python modules).

## Installation

1. Download the `hexstresser.py` file to your local machine.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Open a terminal window.
2. Run the script using the following command:

   ```bash
   git clone https://github.com/Hyezzcraxksz/HexStresser.git
   cd HexStresser
   python HexStresser.py
