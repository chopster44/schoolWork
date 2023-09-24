import os
import copy
from random import randint

screen_height = os.get_terminal_size()[0]
screen_width = os.get_terminal_size()[1]
# screen_height = 24
# screen_width = 80

room_type = list[list[str]]

player_pos: list[int] = [1, 1]

current_room: list[list[str]]

player: str = "@"
enemy: str = "^"
coin: str = "*"
door: str = "+"
wall: list[str] = ["-", "|"]

controls: dict[str, str] = {
    "up": "w",
    "down": "s",
    "left": "a",
    "right": "d",
    "attack": "a",
    "quit": "q"
}


def room_generator(size: int) -> list[list[str]]:
    size = size * 2 + 1
    generated_room: list[list[str]] = [[]]
    for i in range(0, size):
        if i < (size - 1):
            generated_room.append([])
        for j in range(0, size):
            generated_room[i].append(" ")
    for i in range(0, size):
        for j in range(0, size):
            if i == 0 or i == (size - 1):
                generated_room[i][j] = wall[0]
            elif j == 0 or j == (size - 1):
                generated_room[i][j] = wall[1]
            else:
                generated_room[i][j] = " "
    coins: int = randint(1, 5)
    for i in range(0, coins):
        generated_room[randint(1, (size - 2))][randint(1, (size - 2))] = copy.copy(coin)
    return generated_room


def draw_player(pos: list[int], icon: str, game: list[list[str]]):
    out_game: list[list[str]] = copy.deepcopy(game)
    if not (out_game[pos[1]][pos[0]] in wall):
        out_game[pos[1]][pos[0]] = icon
    return out_game


def print_game(game: list[list[str]], pos: list[int]):
    os.system("clear")
    print("\n" * (screen_height - len(game)))
    line: str = "\n"
    for i in game:
        line = ""
        for j in game[game.index(i)]:
            line += j
        print(line)

    print(f"{pos}\nControls:")
    print("Up: w     Down: s     Left: a     Right: d     Attack: (dir)+a    Quit: q\n")


def move(action: str, room: room_type, current_pos: list[int]):
    new_pos: list[int] = copy.deepcopy(current_pos)
    if len(action) > 1:
        if action[1] == controls["attack"]:
            pass
        else:
            return new_pos
    else:
        if action[0] == controls["up"] and (room[(current_pos[1] - 1)][(current_pos[0])] != "-"):
            new_pos = [(current_pos[0]), (current_pos[1] - 1)]
        elif action[0] == controls["down"] and (room[(current_pos[1] + 1)][(current_pos[0])] != "-"):
            new_pos = [(current_pos[0]), (current_pos[1] + 1)]
        elif action[0] == controls["left"] and (room[(current_pos[1])][(current_pos[0] - 1)] != "|"):
            new_pos = [(current_pos[0] - 1), (current_pos[1])]
        elif action[0] == controls["right"] and (room[(current_pos[1])][(current_pos[0] + 1)] != "|"):
            new_pos = [(current_pos[0] + 1), (current_pos[1])]
        elif action[0] == controls["quit"]:
            os.system("clear")
            exit()
    return new_pos


def game_loop(room: room_type, pos: list[int], player_icon: str):
    level = draw_player(pos, player_icon, room)
    print_game(level, pos)
    action: str = input()
    new_pos = move(action, room, pos)
    game_loop(room, new_pos, player_icon)


def start_game():
    global current_room
    current_room = room_generator(randint(3, 15))
    game_loop(current_room, player_pos, player)


start_game()
