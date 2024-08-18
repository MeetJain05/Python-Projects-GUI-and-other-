import turtle
import pandas
screen = turtle.Screen()

screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')

states_name = data.state
states_list = states_name.to_list()
states_guessed_list = []

while len(states_guessed_list) < 50:
    if states_guessed_list == []:
        answer_state = screen.textinput(title='Guess the State', prompt="Enter a State's Name?")
    else:
        answer_state = screen.textinput(title=f'{len(states_guessed_list)}/{len(data.state)} States Correct', prompt="What's another state's name?")
    answer_state_form = answer_state.title()
    
    if answer_state_form == 'Exit':
        missing_states= []
        for state in states_list:
            if state not in states_guessed_list:
                missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    
    if answer_state_form in states_list and answer_state_form not in states_guessed_list:
        states_guessed_list.append(answer_state_form)
        row_state = data[data.state == answer_state_form]
        x_pos = row_state.x
        y_pos = row_state.y

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(int(x_pos),int(y_pos))
        writer.write(answer_state_form)

