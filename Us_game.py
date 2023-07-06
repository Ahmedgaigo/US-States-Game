import turtle
import pandas

FONT = ('Arial', 8, 'normal')
screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(800, 600)

# adding an image
image = 'blank_states_img.gif'
screen.addshape(image)

# reading and storing data in states
states = pandas.read_csv('50_states.csv')

# saved states as list
state_list = states.state.to_list()
correct_guesses = []


while len(correct_guesses) < 50:
	# NB: you have to use the turtle.shape()
	turtle.shape(image)

	# takes input
	answer = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the state", prompt="What's another state?").title()
	if answer == "Exit":
		# creating a csv for states not guessed
		# modifying the code to use a list comprehension
		states_not_guessed = [state for state in state_list if state not in correct_guesses]
		df = pandas.DataFrame(states_not_guessed)
		df.to_csv('states_to_learn.csv')
		break
	if answer in state_list and answer not in correct_guesses:
		# update the list
		correct_guesses.append(answer)

		# getting the row where the correct state is
		position_to_go = states[states.state == answer]

		t = turtle.Turtle()
		t.pu()
		t.hideturtle()
		t.goto(int(position_to_go.x), int(position_to_go.y))
		t.write(answer, False, 'center', FONT)


