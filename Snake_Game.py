import random

WIDTH = 10
HEIGHT = 10

snake = [(5, 5)]
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
score = 0

while True:
    # Display board
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                print("H", end=" ")
            elif (x, y) in snake:
                print("O", end=" ")
            elif (x, y) == food:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()

    print("Score:", score)
    move = input("Move (W/A/S/D): ").upper()

    head_x, head_y = snake[0]

    if move == "W":
        head_y -= 1
    elif move == "S":
        head_y += 1
    elif move == "A":
        head_x -= 1
    elif move == "D":
        head_x += 1
    else:
        print("Invalid move!")
        continue

    new_head = (head_x, head_y)

    # Check wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! You hit the wall.")
        break

    # Check self collision
    if new_head in snake:
        print("Game Over! You hit yourself.")
        break

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        while True:
            food = (random.randint(0, WIDTH - 1),
                    random.randint(0, HEIGHT - 1))
            if food not in snake:
                break
    else:
        snake.pop()

    print("\n" * 3)

print("Final Score:", score)