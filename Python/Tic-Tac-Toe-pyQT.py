import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(300, 300, 300, 400)  # Increase the height to make room for the label

        # Main layout
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        # Game grid layout
        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout, 0, 0)

        # Create buttons for the grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton('')
                button.setFixedSize(80, 80)
                button.setStyleSheet("background-color: #C71585;")
                button.clicked.connect(self.onButtonClicked)
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        # Status label
        self.status_label = QLabel('Player X\'s turn')
        self.status_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.status_label, 1, 0)  # Add label below the grid

        # Set up UI
        self.resetGame()
        self.show()

    def onButtonClicked(self):
        button = self.sender()
        if not button.text():
            current_player = self.players[self.current_player_index]
            button.setText(current_player)
            button.setStyleSheet(f"background-color: #{'FFA07A' if current_player == 'X' else '90EE90'}; color: black;")
            if self.checkWin(current_player):
                self.gameOver(current_player)
            elif self.isBoardFull():
                self.gameOver('Nobody')
            else:
                self.switchPlayer()
                self.updateStatusLabel()

    def switchPlayer(self):
        self.current_player_index = (self.current_player_index + 1) % 2
        self.updateStatusLabel()

    def updateStatusLabel(self):
        current_player = self.players[self.current_player_index]
        self.status_label.setText(f"Player {current_player}'s turn")

    def checkWin(self, player):
        # Check rows, columns, and diagonals for win conditions
        for i in range(3):
            if all(self.buttons[i][j].text() == player for j in range(3)):
                return True
            if all(self.buttons[j][i].text() == player for j in range(3)):
                return True
        if all(self.buttons[i][i].text() == player for i in range(3)) or all(self.buttons[i][2-i].text() == player for i in range(3)):
            return True
        return False

    def isBoardFull(self):
        return all(button.text() for row in self.buttons for button in row)

    def gameOver(self, winner):
     
        self.updateStatusLabel()
        message = f"Player {winner} wins!" if winner != 'Nobody' else "It's a draw!"
        QMessageBox.information(self, "Game Over", message)
        self.resetGame()

    def resetGame(self):
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setStyleSheet("background-color: #C71585;")
        self.players = ['X', 'O']
        self.current_player_index = 0
        self.updateStatusLabel()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())
