# US-States-Game
The U.S. States Game is an educational game developed using Python and the Turtle module. The objective of the game is to guess the names of all 50 U.S. states by clicking on their locations on a blank map of the United States. The game provides an interactive and fun way to learn and test your knowledge of U.S. geography.

Features:

1. Interactive map: The game screen displays a blank map of the United States. You can click on different locations on the map to guess the names of the states.

2. Guessing the states: The game prompts you to enter the name of a state. If your guess is correct, the game highlights the state on the map and displays the name of the state at its correct location.

3. Data handling: The game reads the state data from a CSV file (`50_states.csv`) and stores it as a pandas DataFrame. This data includes the names of the states and their corresponding coordinates on the map.

4. Progress tracking: The game keeps track of your progress by maintaining a list of correct guesses. It shows you the number of states you have guessed correctly out of the total 50.

5. Saving progress: If you want to exit the game, you can enter "Exit" as your guess. The game then saves a CSV file (`states_to_learn.csv`) containing the names of the states that you have not guessed yet.

To play the game, run the script and follow the prompts to guess the names of the U.S. states. Click on the corresponding locations on the map to make your guesses. You can exit the game at any time by entering "Exit".

Enjoy playing the U.S. States Game and have fun while improving your knowledge of U.S. geography!
