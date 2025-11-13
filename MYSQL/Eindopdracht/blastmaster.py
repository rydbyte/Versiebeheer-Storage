import mysql.connector as mysql#importeerd de mysql connector module en noemt het mysql
from datetime import datetime


connection = mysql.connect(#maakt een connectie met de database
    host="127.0.0.1",
    user="root",
    password="Tweedinosdiedansen2!",
    database="games"
)

connection.autocommit = True#autocmmit zodat alles word opgeslagen
cursor = connection.cursor(dictionary=True)#connections cursor variable dict true zodat de returned value als dict terug komt


def menu():#functie voor het menu
    print("\n################################################\nWelcome to the Menu\n")#print een welkom bericht
    choice = ""#variable voor keuze
    while choice not in  ["1","2","3","4","5","6","7","8"]:#loopt zolang choice niet 1 tm 8 is
        choice = input("1. Insert Player\n2. Insert Game\n3. Insert Highscore\n4. All Games\n5. All Players\n6. All Highscores\n7. Players Highscores\n8. Game Earnings \nPick a Number: ")# input en weergeeft opties
        if choice not in ["1","2","3","4","5","6","7","8"]:#als choice niet 1 tm 8 is print een bericht
            print("Pick between 1/2/3/4/5/6/7/8\n")
    defs[int(choice)]()#als de keuze dus wel 1 of tm 8 is dan stopt de while loop en begint dit veranderd de choice naar een int en start de functie uit de list

def back():# na elke functie gebruikt om de vrage of user terug naar menu wilt
     back_y_n = input("\n################################################\n\nBack to Menu?\n1. Yes\n2. No\n")
     if back_y_n != "2":# als p alles behalve str 2 is
        menu()#terug naar menu
     else:#anders als het wel 2 is
        sure = input("Not going back closes the program, are you sure:\n1. Yes\n2. No\n")
        if sure == "1":
            exit()#stopt programma
        else:
            back()

def insert_player():# functie voor een nieuwe speler toevoegen aan de database
    print("\n################################################\n")# print dit zodat het er overzichtelijker uitziet
    name = ""# naam variable
    while name == "":# zolang de naam "" is, vraag om input voor de naam
        name = input("\nPlayers Name: ").capitalize()#vraagt om input voor de naam en capitalized het zodat de eerste letter altijd een hoofdletter is
    
    cursor.execute("select player_id from player;")#gaat naar de mysql cursor en selecteert de player_ids van de player tabel
    cursor.fetchall()#fecthall pakt alle informatie
    amount = cursor.rowcount#de totaale hoeveelheid ids
    cursor.execute("insert into player(player_id, player_name, email) values(%s,%s,%s)", (amount+1, name, name+"@blastmaster.nova"))#opnieuw execute in mysql values %s voor temp dan daarna de values die erin gaan
    print(f"Player: {name} Added")#print zodart de user weet dat een speler is toegevoegd
    back()#terug nar menu functie

def insert_game():# inser game functie
    print("\n################################################\n")
    game_name = ""#game_name variable
    genre = ""#genre1
    genre2 = "a"#genre2
    price = 1#de prijs van de game
    while game_name == "":#zolang de game name "" is vraag om een game name
        game_name = input("Game Name: ")
    while genre not in ["maze", "shoot `em up", "platform", "fighting", "puzzle", "sports", "run and gun", "light gun shooter"]:#loopt totdat er een genre die in de lijst staat word ingevoerd
        print("\nGenres: Maze, Shoot `em up, Platform, Fighting, Puzzle, Sports, Run and Gun, Light Gun Shooter")#laat alle genres zien
        genre = input("Genre: ").lower()#maakt de input allemaal lowcase
    while genre2 not in ["","maze", "shoot `em up", "platform", "fighting", "puzzle", "sports", "run and gun", "light gun shooter"] or genre2 == genre:#zolang genre 2 niet in de lijst staat of zolang het hetzelfde is als genre1
        print("\nGenres: Maze, Shoot `em up, Platform, Fighting, Puzzle, Sports, Run and Gun, Light Gun Shooter(Laat leeg voor geen tweede genre)")#print de rij van genres
        genre2 = input("Genre 2: ").lower()
        if genre2 == genre:#als genre2 jhezelfde is als genre1 dan print warning
            print("Cant have the same Genre")
        if genre2 != "":#als genre2 alles behalve de str"" is s de prijs 1.5 sinds er een tweede genre is
            price = 1.5
        elif genre2 == "":#anders als het genre2 str "" is maakt de prijs 1
            price = 1
    cursor.execute("select game_id from game;")#selecteerd de game_id van tabel game in mysql
    cursor.fetchall()#pakt alle terug gegeven data
    amount = cursor.rowcount#returned totale hoeveelheid ids 
    cursor.execute("insert into game(game_id, Game_name, genre, genre2, price) values(%s,%s,%s,%s,%s)", (amount+1, game_name, genre, genre2, price))#stopt nieuwe dingen in tabel game id is de amount+1 zodat het altijd een nieuwe id is 
    print(f"Game: {game_name} Added\nPrice: ${price}")# laat zien aan de user dat de game is toegevoegd met de prijs
    back()#terug naar menu

def insert_score():#scoren toevoegen
    print("\n################################################\n")
    limit = 0
    game_id = ""
    player_id = ""
    highscore_datum = ""
    pogingen = ""

    cursor.execute("select game_id from game")#game id
    cursor.fetchall()#returned alle ids
    a = cursor.rowcount# a = de totale hoeveelheid ids

    cursor.execute("select game_id, game_name from game")
    all = cursor.fetchall()
    for row in all:#for loop door alle colums
        print(str(row["game_id"])+".", row["game_name"])#print de id en de naam van elke collumm
    while not game_id.isnumeric() or int(game_id) <1 or int(game_id) > a:#loopt zolang game_id niet een nummer is of zolang de game_id onder 1 is of hoger is dan de totale hoeveeilheid ids
        game_id = input("Type the number of which game this highscore was achieved in: ")#vraagt om input van de game id
        if not game_id.isnumeric() or int(game_id) <1 or int(game_id) > a:#zelfde als de loop maar geeft warning terug 
            print("Unable to find this game number.")

    
    cursor.execute("select player_id from player")#is een copy van game id(hier boven) maar inplaats van game id, player id
    cursor.fetchall()
    a = cursor.rowcount

    cursor.execute("select player_id, player_name from player")
    all = cursor.fetchall()
    for row in all:
        print(str(row["player_id"])+".",row["player_name"])
    while not player_id.isnumeric() or int(player_id) <1 or int(player_id) > a:
        player_id = input("Type de spelers nummer in waarvan je de highscore wilt invoegen: ")
        if not player_id.isnumeric() or int(player_id) <1 or int(player_id) > a:
            print("Unable to find this player number.")
    
    highscore = input("Wat is de highscore: ")#vraagt om input voor highscore
    while not highscore.isnumeric():#loopt zolang de highscore niet een nummer is
        print("Only numberts allowed.")#print warning
    
        highscore = input("What is the highscore: ")#vraagt opnieuw naar input
    while highscore_datum == "" or len(highscore_datum) < 8:#loopt voor highscore datum
        highscore_datum = input("Enter datum yyyy/mm/dd: ")#vraagt een datum van behaling highscore
        if  len(highscore_datum) < 8:
            print("Enter valid date")
    
    pogingen = input("Hoeveel pogingen zijn er gedaan: ")#vraagt om aantal pogingen
    while not pogingen.isnumeric() or int(pogingen) <= 0:#als de pogingen geen nummer is of gelijk of onder 0 zit blijft loopen
        print("Alleen nummers en niet onder 1")
        pogingen = input("How many attempts: ")

    cursor.execute("select * from game join highscore on highscore.game_id = game.game_id join player on player.player_id = highscore.player_id")
    all = cursor.fetchall()
    if len(all) == 0 and limit == 0:
         limit = 1
         cursor.execute("insert into highscore(game_id, player_id, pogingen, highscore, highscore_datum) values(%s,%s,%s,%s,%s)", (int(game_id), int(player_id), int(pogingen), int(highscore), highscore_datum))#execute voor nieuwe highscore voert de game id in de player id de hoeveelheid pogingen de highscore en wanneeer de highscore is behaalt
         print(f"\nPlayer ({player_id}) highscore ({highscore}) added to game ({game_id})\nAmount of attempts: {pogingen}\nDate: {highscore_datum}")#print zodat de user kant zien wat er toegevoegd is
    else:
        for row in all:
            print("a")
            if row["game_id"] == int(game_id) and row["player_id"] == int(player_id) and limit == 0:
                if int(highscore) < row["highscore"]:
                    print("This highscore is lower.")
                    limit = 1
                    back()
                else:
                    cursor.execute(f"update highscore set highscore = %s, highscore_datum = %s, pogingen = %s where game_id = %s", (int(highscore), highscore_datum, int(pogingen) + int(row["pogingen"]), game_id))
                    print(f"\nPlayer ({player_id}) highscore ({highscore}) updated on game ({game_id})\nAmount of attempts: {pogingen}\nDate: {highscore_datum}")
                    limit = 1
            elif not row["game_id"] == int(game_id) and limit == 0 or not row["player_id"] == int(player_id) and limit == 0:
                limit = 1
                cursor.execute("insert into highscore(game_id, player_id, pogingen, highscore, highscore_datum) values(%s,%s,%s,%s,%s)", (int(game_id), int(player_id), int(pogingen), int(highscore), highscore_datum))#execute voor nieuwe highscore voert de game id in de player id de hoeveelheid pogingen de highscore en wanneeer de highscore is behaalt
                print(f"\nPlayer ({player_id}) highscore ({highscore}) added to game ({game_id})\nAmount of attempts: {pogingen}\nDate: {highscore_datum}")#print zodat de user kant zien wat er toegevoegd is

    back()#terug naar menu

def all_games(): # laat alle games zien 
    print("\n################################################\n")
    cursor.execute("select * from game")#selecteert alles van de tabel game
    results = cursor.fetchall()#returned info van tabel
    for row in results:#loopt door de returned info
        if row["genre2"] == "":#als genre2 er niet is print deze string
            print(str(row["game_id"])+".", row["game_name"]+",", row["genre"]+",","$"+str(row["price"]))
        elif not row["genre2"] == "":#als de tweede genre er wel is print deze str
            print(str(row["game_id"])+".", row["game_name"]+",", row["genre"]+"/", row["genre2"]+",","$"+str(row["price"]))

    back()#terugggg naar menu

def all_players():#laat alle spelers zien
    print("\n################################################\n")
    cursor.execute("select * from player")#sleecteert alles van tabel player
    players = cursor.fetchall()#pakt alle collommen
    for player in players:# voor de hoeveelheid in tabel player  print de players id de players naam en de email
        print(str(player["player_id"])+".",player["player_name"]+",",player["email"])

    back()#terug

def all_highscores():#laat alle highscore zien
    print("\n################################################\n")
    cursor.execute("select game.game_name, player.player_name, highscore.highscore, highscore.highscore_datum from game join highscore on highscore.game_id = game.game_id join player on highscore.player_id = player.player_id order by game.game_name")#joined de tabel game, player en highscore samen en pakt daar dan data van
    all = cursor.fetchall()
    game_name = ""
    rowcount = cursor.rowcount
    if rowcount == 0 :#als er geen data terug is gekomen zijn er geen highscores
            print("\nNog geen highscores")
    else:#als er wel highscores zijn print met een for loop de naam speler naam highscore en datum van highscore
        for row in all:
            if row["game_name"] != game_name:
                game_name = row["game_name"]
                print("\n")
                print(row["game_name"])
                
            print(row["player_name"]+",", str(row["highscore"])+"P"+",",str(row["highscore_datum"]))
    back()

def player_highscore():#laat de alle players highscores zien
    print("\n################################################\n")
    cursor.execute("select player.player_name, game.game_name, highscore.highscore from player join highscore on highscore.player_id = player.player_id join game on game.game_id = highscore.game_id order by highscore.highscore desc")#joined alle tabels en ordered ze bij de hoogste highscore
    all = cursor.fetchall()
    highscore = -1
    for row in all:
        if row["highscore"] != highscore:
            highscore = row["highscore"]
            print("\n")
            print(str(row["highscore"])+"P")
           
        print(row["player_name"]+",", row["game_name"])
    
    back()

def earnings():
    print("\n################################################\n")
    games = []#storage for games

    cursor.execute("select game_id, game_name, price from game")#select voor games
    all = cursor.fetchall()
    for row in all:#looped door alle dicts
        if not row in games:#als de dict niet in de list games zit stopt hem erin
            games.append(row)
        elif row in games:#anders passed
            pass
    
    cursor.execute("select sum(highscore.pogingen), game.game_name from highscore join game on game.game_id = highscore.game_id group by game.game_id")#selecteerd de totale hoeveelheid pogingen van elke game 
    pogingen = cursor.fetchall()#returned alle pogingen met game
   
    for row in pogingen:#for dict in pogingen
        for game in games:#looped door de list met dicts van games
            if row["game_name"] == game["game_name"]:#als de namen van de twee dicts hetzelfde zijn past de prijs aan 
                game["price"] *= float(row["sum(highscore.pogingen)"])

    for row in games:#voor alle dicts in games
        print(row["game_name"])#print de game naam van de dict
        print("$"+str(row["price"]))      #print de prijs in dit geval de hoeveeilheid geld verdient met een $ ervoor

    back()   #gaat weer terug       

defs = ["",insert_player, insert_game, insert_score, all_games, all_players, all_highscores, player_highscore, earnings]#de list met alle functies erin
menu()#functie voor het starten van menu