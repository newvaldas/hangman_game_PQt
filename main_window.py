import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication
from ui_hangman import Ui_MainWindow
from game_data import GameData


class MainWindow:
    def __init__(self) -> None:
        """
        Initialize game window
        """
        # ----- setup UI elements ----- #
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        # ----- initialize game variables ----- #
        self.db = GameData()
        self.word = ""
        self.guessed_word = []
        self.misses = 0
        
        # ----- initialize game UI with starting values ----- #
        self.choose_word()
        self.display_guesses()
        self.display_gallows()
        self.signals()
       
        

    def show(self) -> None:
        """
        Displays main window
        """
        self.main_win.show()
        
        
    def choose_word(self) -> str:
        """
        Gets word from gamedata and creats a list for guessed letters
        """
        self.word = self.db.get_word()
        self.guessed_word = ["_"] * len(self.word)
        
        
    def display_guesses(self) -> str:
        """
        Display guessed letters in UI
        """
        display_word = ""
        for character in self.guessed_word:
            display_word = display_word + character + " "    
            
        self.ui.word_lb.setText(display_word)
        
            
    def display_gallows(self) -> None:
        """
        Displays hangman progression to UI
        """
        file_name = (f"./images/{self.misses}.png")
        gallow = QPixmap(file_name)
        self.ui.gallow_lb.setPixmap(gallow)
        
    def set_button_enabled(self, val):
        
        self.ui.a_btn.setEnabled(val)
        self.ui.b_btn.setEnabled(val)
        self.ui.c_btn.setEnabled(val)
        self.ui.d_btn.setEnabled(val)
        self.ui.e_btn.setEnabled(val)
        self.ui.f_btn.setEnabled(val)
        self.ui.g_btn.setEnabled(val)
        self.ui.h_btn.setEnabled(val)
        self.ui.i_btn.setEnabled(val)
        self.ui.j_btn.setEnabled(val)
        self.ui.k_btn.setEnabled(val)
        self.ui.l_btn.setEnabled(val)
        self.ui.m_btn.setEnabled(val)
        self.ui.n_btn.setEnabled(val)
        self.ui.o_btn.setEnabled(val)
        self.ui.p_btn.setEnabled(val)
        self.ui.q_btn.setEnabled(val)
        self.ui.r_btn.setEnabled(val)
        self.ui.t_btn.setEnabled(val)
        self.ui.s_btn.setEnabled(val)
        self.ui.u_btn.setEnabled(val)
        self.ui.v_btn.setEnabled(val)
        self.ui.w_btn.setEnabled(val)
        self.ui.x_btn.setEnabled(val)
        self.ui.y_btn.setEnabled(val)
        self.ui.z_btn.setEnabled(val)
        
    
    
        
    def signals(self) -> None:
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        self.ui.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.new_word_btn.clicked.connect(self.new_word_btn)
        
        # letter buttons
        self.ui.a_btn.clicked.connect(lambda: self.letter_btn(self.ui.a_btn))
        self.ui.b_btn.clicked.connect(lambda: self.letter_btn(self.ui.b_btn))
        self.ui.c_btn.clicked.connect(lambda: self.letter_btn(self.ui.c_btn))
        self.ui.d_btn.clicked.connect(lambda: self.letter_btn(self.ui.d_btn))
        self.ui.e_btn.clicked.connect(lambda: self.letter_btn(self.ui.e_btn))
        self.ui.f_btn.clicked.connect(lambda: self.letter_btn(self.ui.f_btn))
        self.ui.g_btn.clicked.connect(lambda: self.letter_btn(self.ui.g_btn))
        self.ui.h_btn.clicked.connect(lambda: self.letter_btn(self.ui.h_btn))
        self.ui.i_btn.clicked.connect(lambda: self.letter_btn(self.ui.i_btn))
        self.ui.j_btn.clicked.connect(lambda: self.letter_btn(self.ui.j_btn))
        self.ui.k_btn.clicked.connect(lambda: self.letter_btn(self.ui.k_btn))
        self.ui.l_btn.clicked.connect(lambda: self.letter_btn(self.ui.l_btn))
        self.ui.m_btn.clicked.connect(lambda: self.letter_btn(self.ui.m_btn))
        self.ui.n_btn.clicked.connect(lambda: self.letter_btn(self.ui.n_btn))
        self.ui.o_btn.clicked.connect(lambda: self.letter_btn(self.ui.o_btn))
        self.ui.p_btn.clicked.connect(lambda: self.letter_btn(self.ui.p_btn))
        self.ui.q_btn.clicked.connect(lambda: self.letter_btn(self.ui.q_btn))
        self.ui.r_btn.clicked.connect(lambda: self.letter_btn(self.ui.r_btn))
        self.ui.s_btn.clicked.connect(lambda: self.letter_btn(self.ui.s_btn))
        self.ui.t_btn.clicked.connect(lambda: self.letter_btn(self.ui.t_btn))
        self.ui.u_btn.clicked.connect(lambda: self.letter_btn(self.ui.u_btn))
        self.ui.v_btn.clicked.connect(lambda: self.letter_btn(self.ui.v_btn))
        self.ui.w_btn.clicked.connect(lambda: self.letter_btn(self.ui.w_btn))
        self.ui.y_btn.clicked.connect(lambda: self.letter_btn(self.ui.y_btn))
        self.ui.z_btn.clicked.connect(lambda: self.letter_btn(self.ui.z_btn))       
    
    # ----- slots ----- #
    def new_word_btn(self) -> None:
        """
        Chooses a new word and reset UI
        """
        #  gets new word
        self.choose_word()
        self.display_guesses()
        #  reset GUI
        self.misses = 0
        self.display_gallows()
        self.set_button_enabled(True)
        self.ui.result_lb.setText("")
        
    def letter_btn(self, button) -> None:
        """
        Disables the clicked button, cheks if letter is in the word,
        cheks game status
        """
        # get letter
        guess = button.text().lower() 
      
        # disable letter
        button.setEnabled(False)
        
        # check letter in word
        if guess in self.word:
            for index, letter in enumerate(self.word): # add guess to guessed_word
                if guess == letter:
                    self.guessed_word[index] = guess.upper()
            self.display_guesses # display guessed_word
            
            if "_" not in self.guessed_word: #check for win
                self.ui.result_lb.setText("You are Winner!")
        else:
            # add misses count, update GUI and cheks if game over
            self.misses += 1
            self.display_gallows()
            # check for loss
            if self.misses == 10:
                self.ui.result_lb.setText(f"The word was {self.word.upper()}")
                self.set_button_enabled(False)
         


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())