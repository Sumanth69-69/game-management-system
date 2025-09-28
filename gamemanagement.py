# In-memory data structures
games = []
players = {}


# Recruiter Functions
def create_game():
    game_id = len(games) + 1
    name = input("Enter game name: ")
    requirements = input("Enter requirements: ")
    time = input("Enter time: ")
    place = input("Enter place: ")
    slots = int(input("Enter number of slots: "))

    game = {
        "id": game_id,
        "name": name,
        "requirements": requirements,
        "time": time,
        "place": place,
        "slots": slots,
        "players": []
    }
    games.append(game)
    print(f"Game '{name}' created successfully!")


def edit_game():
    game_id = int(input("Enter game ID to edit: "))
    for game in games:
        if game["id"] == game_id:
            game["name"] = input("Enter new name: ") or game["name"]
            game["requirements"] = input("Enter new requirements: ") or game["requirements"]
            game["time"] = input("Enter new time: ") or game["time"]
            game["place"] = input("Enter new place: ") or game["place"]
            slots = input("Enter new slots: ")
            if slots:
                game["slots"] = int(slots)
            print("Game updated successfully!")
            return
    print("Game not found!")


def delete_game():
    game_id = int(input("Enter game ID to delete: "))
    global games
    games = [g for g in games if g["id"] != game_id]
    print("Game deleted successfully!")


# Player Functions
def view_games():
    if not games:
        print("No games available!")
        return
    for game in games:
        print(
            f"ID: {game['id']}, Name: {game['name']}, Slots Left: {game['slots'] - len(game['players'])}, Time: {game['time']}, Place: {game['place']}")


def register_game():
    player_name = input("Enter your name: ")
    game_id = int(input("Enter game ID to register: "))

    for game in games:
        if game["id"] == game_id:
            if len(game["players"]) < game["slots"]:
                game["players"].append(player_name)
                players[player_name] = game_id
                print(f"{player_name} registered for {game['name']}")
            else:
                print("No slots available!")
            return
    print("Game not found!")


def cancel_registration():
    player_name = input("Enter your name: ")
    if player_name in players:
        game_id = players[player_name]
        for game in games:
            if game["id"] == game_id:
                if player_name in game["players"]:
                    game["players"].remove(player_name)
                    del players[player_name]
                    print(f"{player_name} cancelled registration from {game['name']}")
                    return
    print("Player not registered!")


# Main Menu
def main():
    while True:
        print("\n1. Recruiter\n2. Player\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\n1. Create Game\n2. Edit Game\n3. Delete Game\n4. Back")
            r_choice = input("Enter choice: ")
            if r_choice == "1":
                create_game()
            elif r_choice == "2":
                edit_game()
            elif r_choice == "3":
                delete_game()

        elif choice == "2":
            print("\n1. View Games\n2. Register\n3. Cancel Registration\n4. Back")
            p_choice = input("Enter choice: ")
            if p_choice == "1":
                view_games()
            elif p_choice == "2":
                register_game()
            elif p_choice == "3":
                cancel_registration()

        elif choice == "3":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
