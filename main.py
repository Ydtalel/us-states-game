import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []


def print_state():
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x_cor, y_cor)
    text.write(answer_state, align='center', font=('Arial', 6, 'normal'))


data = pandas.read_csv("50_states.csv")
name_state = data['state'].tolist()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in name_state if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states to learn.csv")
        break
    if answer_state in name_state:
        state_row = data[data.state == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        print_state()
        # answer_state is the same state.row_state.item()
        guessed_states.append(answer_state)

#states to learn.csv




# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()



screen.exitonclick()