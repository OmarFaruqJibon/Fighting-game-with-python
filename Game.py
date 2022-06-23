import random
import time

rounds = 1
enemy_win = 0
player_win = 0

while rounds <= 3:
    print(f'\n\t\t\t--------Now it\'s Round {rounds} --------\n')
    time.sleep(1)

    print('[Player]')
    player_hp = random.randint(100, 150)
    player_att = random.randint(20, 50)
    print(f'Heath Point: {player_hp}')
    print(f'Attack: {player_att}')
    print('-------------------------------------------------------------------\n')
    time.sleep(1)

    print('[Enemy]')
    enemy_hp = random.randint(100, 150)
    enemy_att = random.randint(20, 50)
    print(f'Heath Point: {enemy_hp}')
    print(f'Attack: {enemy_att}')
    print('-------------------------------------------------------------------\n')
    time.sleep(1)

    while player_hp >= 0 and enemy_hp >= 0:
        enemy_hp = enemy_hp - player_att
        player_hp = player_hp - enemy_att
        print(f'You are attacking enemy, [Enemy\'s] remain health point is: {enemy_hp}')
        print(f'Enemy is attacking you, [Player\'s] remain health point is: {player_hp}')
        print('-------------------------------------------------------------------\n')
        time.sleep(1)
        continue

    # checking winner for each rounds
    if player_hp <= 0 and enemy_hp <= 0:
        print('You and Enemy were died both !\n\n')
    elif player_hp <= 0:
        print('Enemy Win !\n\n')
        enemy_win += 1
    else:
        print('You Win !\n\n')
        player_win += 1
    time.sleep(1)

    rounds += 1

print('\t\t\t--------Game Over--------\n\n')

# checking final winner and looser
if player_win == enemy_win:
    print('Game draw !\n')
elif player_win > enemy_win:
    print('Final Winner: You !\nLooser: Enemy !\n')
else:
    print('Final Winner: Enemy !\nLooser: You !\n')


