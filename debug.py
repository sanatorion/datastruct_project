import cursor, animation

number = 13
i = 0
hp = 10

input()
print(f"\r✚ Health: {hp} (+{number})")
animation.time.sleep(1)

print('\033[F\033[2K', end = '')
while i < number:
    print(f"\r✚ Health: {hp} (+{number})")
    number -= 1
    hp += 1
    animation.time.sleep(0.1)
    print('\033[F\033[2K', end = '')
print(f"\r✚ Health: {hp}")
input()
    