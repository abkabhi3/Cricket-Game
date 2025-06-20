import random

normal_balls = ['0', '0', '1','1', '2', '2', '3', '4', '6', 'W', 'Wide', 'No Ball']
free_hit_balls = ['0', '1', '2', '3', '4', '6', 'Run Out']

overs = int(input("Enter number of overs: "))
balls_per_over = 6
total_balls = overs * balls_per_over

score = 0
wickets = 0
ball_count = 0
player = 1
free_hit = False

print("\n--- Match Start ---")
print("Press Enter to bowl each ball...\n")

while ball_count < total_balls and wickets < 10:
    input(f"🎯 Ball {ball_count + 1} | Player {player} - Press Enter to bowl: ")

    if free_hit:
        result = random.choice(free_hit_balls)
    else:
        result = random.choice(normal_balls)

    print(f"Result: {result}")

    if result == 'W':
        if free_hit:
            print("Free hit - Wicket ignored!\n")
        else:
            wickets += 1
            print(f"Player {player} is OUT!\n")
            player += 1
    elif result == 'Run Out':
        wickets += 1
        print(f"Player {player} is RUN OUT!\n")
        player += 1
    elif result == 'Wide' or result == 'No Ball':
        score += 1
        print("Extra Run!")
        if result == 'No Ball':
            free_hit = True
        continue 
    else:
        score += int(result)
        if free_hit:
            free_hit = False
        print()

    ball_count += 1

print("\n--- Innings Over ---")
print(f"Total Score: {score}/{wickets}")
print(f"Overs Played: {ball_count // 6}.{ball_count % 6}")