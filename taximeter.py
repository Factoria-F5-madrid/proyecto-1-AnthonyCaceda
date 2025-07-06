import time

# variables bienvenida:
welcome = "¡Hi, welcome to Automad! \n"
explanation = "Thank you for using our services, here is a list of keywords to use in our program: start, move, stop, finish and exit."
# variables para mi operacion:
start_time = 0
stopped_time = 0
moving_time = 0
trip_active = False
print(welcome, explanation)
user_input = ""
while True:  # bucle inifito y verdadero, se rompe con break
    user_input = input(":").strip().lower()  # pedir al usuario que ingrese algo
    if user_input == "start":  # si el usuario escribe start
        if trip_active:
            print("Error: A trip is already in progress.")
            continue
        trip_active = True
        start_time = time.time()
        stopped_time = 0
        moving_time = 0
        state = "stopped"  # Iniciamos en estado 'stopped'
        state_start_time = time.time()
        print("Trip started. Initial state: 'stopped'.")

    elif user_input in ("stop", "move"):
        if not trip_active:  # si trip_active = false
            print("Error: No active trip. Please start first.")
            continue
        # Calcula el tiempo del estado anterior
        duration = time.time() - state_start_time
        if state == "stopped":  # si hasta ahora estabamos en stop
            stopped_time = stopped_time + duration  # incremetar el tiempo total de stop
        else:  # si hasta ahora estabamos en move
            moving_time = stopped_time + duration  # incremetar el tiempo total de move

        # Cambia el estado
        if user_input == "stop":
            state = "stopped"
        else:
            state = "moving"
        state_start_time = time.time()
        print(f"State changed to '{state}'.")

    elif user_input == "finish":
        if not trip_active:
            print("Error: No active trip to finish.")
            continue
            # Agrega tiempo del último estado
        duration = time.time() - state_start_time
        if state == "stopped":
            stopped_time += duration
        else:
            moving_time += duration
        # Calcula el precio total
        total_fee = stopped_time * 0.02 + moving_time * 0.05
        print("**************************")
        print("total: ", round(total_fee, 3), "€")
        print("**************************")
        trip_active = False
        state = ""
    elif user_input == "exit":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Unknown command. Use: start, stop, move, finish, or exit.")
