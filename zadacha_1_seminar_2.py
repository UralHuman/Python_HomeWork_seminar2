num_coins = int(input("Введите колличество монеток: "))

eagle_side = 0
side_tails = 0

for i in range(1, num_coins + 1):
    coin = int(input(f"Монетка № {i}: "))
    if coin == 1:
        eagle_side += 1
    elif coin == 0:
        side_tails += 1
print(f'Минимальное колличество: {min(eagle_side,side_tails)} монетки')
