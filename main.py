from collections import deque

def maze_yechish(maze, bosh_nokta, tugun):
    q = deque()
    q.append(bosh_nokta)
    kochalar = {bosh_nokta: None}

    while q:
        x, y = q.popleft()

        if (x, y) == tugun:
            yo'l = []
            while (x, y) != bosh_nokta:
                yo'l.append((x, y))
                x, y = kochalar[(x, y)]
            yo'l.append(bosh_nokta)
            yo'l.reverse()
            return yo'l

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(maze)) and (0 <= ny < len(maze[0])) and maze[nx][ny] == 0 and (nx, ny) not in kochalar:
                q.append((nx, ny))
                kochalar[(nx, ny)] = (x, y)

    return None

# Misol:
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

bosh_nokta = (0, 0)
tugun = (4, 4)

print(maze_yechish(maze, bosh_nokta, tugun))
```

Kodda quyidagilar mavjud:

- `maze_yechish` funksiyasi labirint yechish uchun mo'ljallangan.
- Funksiya `maze` (labirint) matritsasi, `bosh_nokta` (bosh nishoni) va `tugun` (tugan nishoni) koordinatalarini qabul qiladi.
- Funksiya `q` deq (kuyruq) obyekti yaratib, unda bosh nishonni qo'yadi.
- Funksiya `kochalar` (kochalar) slovarya joylashtiradi, unda har bir nishonning oldingi nishoni saqlanadi.
- Funksiya `while` tsikli orqali kuyruqdan nishonlarni olib, ularning oldingi nishonlariga borib, tugan nishonni topguncha yuradi.
- Funksiya tugan nishon topilganida, yo'lni qaytaradi.
- Funksiya tugan nishon topilmaganida, `None` qaytaradi.
- Misol uchun, `maze` matritsasi, `bosh_nokta` va `tugun` koordinatalari kiritiladi va `maze_yechish` funksiyasi chaqiriladi.
