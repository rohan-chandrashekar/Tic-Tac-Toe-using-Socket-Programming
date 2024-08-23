
# 🎮 Tic-Tac-Toe Game with Socket Programming 🎮

Welcome to the **Tic-Tac-Toe Game** built using Python, featuring client-server architecture via socket programming. This project showcases how two systems, running separately, can interact over a network using sockets to simulate a classic game of Tic-Tac-Toe.

## 🛠️ Project Overview

This Tic-Tac-Toe game is a network-based multiplayer game where the **client** and **server** are located on two separate machines and communicate using socket programming over TCP/IP. The client can challenge the server repeatedly, and the results of each game are stored locally using a file system, allowing users to view their game history.

### ✨ Key Features:

- **Client-Server Architecture:** The game uses socket programming to enable communication between two systems over a network.
- **Multiple Game Sessions:** The client can challenge the server as many times as desired without restarting the program.
- **Persistent Game Records:** The outcome of each game (win, lose, draw) is stored in a file system, allowing players to track their performance.
- **Cross-Machine Compatibility:** The server and client can run on different machines, with IP addresses set accordingly in the code.
- **Dynamic Challenge System:** The client initiates a new challenge, and the server responds, ensuring real-time interaction.
  
## 🚀 Getting Started

### 1. **Prerequisites:**
- Python 3.x installed on both client and server machines.
- A network connection between the client and server machines.

### 2. **Setting Up:**

- **Server**:
  - Run the `server.py` file on the server machine:
    ```bash
    python3 server.py
    ```
  
- **Client**:
  - Modify the IP address in the `client.py` file to match the server's IP address.
  - Run the `client.py` file on the client machine:
    ```bash
    python3 client.py
    ```

### 3. **Playing the Game:**

- Once the client connects to the server, the game begins with a familiar 3x3 grid displayed on both the client and server terminals.
- Players take turns to place their marks ('X' or 'O') on the grid. The game checks for win conditions (three in a row: horizontally, vertically, or diagonally) and updates the grid in real time.
- The result of each game is saved locally for post-game analysis.

### 4. **Viewing Game Results:**

After each game, the results are stored in a file system. Players can view the outcome of their past games by accessing the result file in their local system.

## 💾 File Structure

```bash
tic-tac-toe-socket-game/
│
├── client.py           # Handles the client-side game logic and connects to the server.
├── server.py           # Runs the game server, handles requests from the client.
└── tic_tac_toe.py      # Core game logic, includes the grid display and game outcome determination.
```

### 📝 Code Explanation

1. **client.py**:
   - Initiates a connection with the server using sockets.
   - Sends and receives game moves from the server.
   - Displays the updated game board after each move.
   - Requests a rematch upon completion of a game.

2. **server.py**:
   - Listens for client connections and initializes a game session when a client connects.
   - Processes the client's moves and updates the game state.
   - Sends the game board status to the client.
   - Saves the game result to the file system after each game.

3. **tic_tac_toe.py**:
   - Contains the logic to handle the Tic-Tac-Toe game rules, including win condition checks and board management.

## 🌐 Network Configuration

To connect the client and server over a network, ensure the following:

- **Client IP Configuration**: The client machine should have the correct IP address of the server configured in the code.
- **Network Port**: Make sure that both machines are on the same network or accessible to each other (check firewall and port settings if needed).
- **Socket Connection**: The project uses the TCP/IP socket protocol to ensure reliable communication between the client and server.

## 🛠️ How It Works

1. **Game Flow**: 
   - When the client connects to the server, a game session is initiated.
   - Players alternate turns to place their symbol ('X' or 'O') on a 3x3 grid.
   - The server determines the winner and sends the result back to the client.
   - Both players can play as many games as they wish within the same session.

2. **Persistent Data**: 
   - After each game, the result (win/lose/draw) is stored locally on both client and server machines for record-keeping purposes.
  
## 🎯 Project Intent

This project is designed to demonstrate the use of Python's socket programming to implement a real-time multiplayer game over a network. It highlights essential skills in network programming, inter-process communication, and file handling, making it suitable for academic presentations and as part of your professional portfolio.

## 🔧 Customization

Feel free to enhance the project with additional features like:

- **Graphical User Interface (GUI):** Implement a GUI using libraries like Tkinter or PyQt for a more user-friendly experience.
- **Scoreboard:** Create a scoreboard to display win-loss statistics across multiple game sessions.
- **AI Player:** Add an AI opponent to make the game more challenging when the server is idle.
