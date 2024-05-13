import turtle
import pandas
from Writer import Writer

screen = turtle.Screen()
screen.title("US States Game")

#criar a imagem de fundo para tela do jogo com o mapa dos USA
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#criar tartaruga invisível responsável por escrever os nomes dos estados
turtle_writer = Writer()

#lista vazia para manter controle dos estados advinhados
states_guessed = []

#ler dados do csv
states_full_data = pandas.read_csv("50_states.csv")
list_of_states = states_full_data["state"]



game_is_on = True

while game_is_on:
    score = f"{len(states_guessed)}/{len(list_of_states)}"
    answer_state = screen.textinput(title=f"{score} States guessed", prompt="What's another state name?").title()
    for loop_state in list_of_states:
        if answer_state == loop_state and loop_state not in states_guessed:
            states_guessed.append(loop_state)
            x_state = int(states_full_data.x[states_full_data.state == loop_state])
            y_state = int(states_full_data.y[states_full_data.state == loop_state])
            turtle_writer.walk_to_state(x_state, y_state)
            turtle_writer.write_state_name(state_name=loop_state)





turtle.mainloop()