#target area: x=102..157, y=-146..-90
min_target_x = 102
max_target_x = 157
min_target_y = -146
max_target_y = -90

# Sample
#min_target_x = 20
#max_target_x = 30
#min_target_y = -10
#max_target_y = -5

def is_within_target(point):
    (x, y) = point
    return min_target_x <= x <= max_target_x and min_target_y <= y <= max_target_y

def simulate_trajectory(velocity, max_y):
    x, y = 0, 0
    (dx, dy) = velocity
    while(not is_within_target((x, y)) and x <= max_target_x and y >= min_target_y):
        max_y = max(max_y, y)
        x += dx
        y += dy
        dy -= 1
        dx -= 0 if dx == 0 else 1 if dx > 0 else -1
    return (x, y, is_within_target((x, y)), max_y)

highest_y = float('-inf')
velocities = set()
for dy in range(min_target_y,1000):
    for dx in range(1, max_target_x + 1):
        (x, y, hit_target, max_y) = simulate_trajectory((dx, dy), highest_y)
        if hit_target:
            if max_y > highest_y:
                highest_y = max_y
            velocities.add((dx, dy))
            print(f'velocity ({dx},{dy}) did hit target in ({x},{y}) with max Y = {max_y}')

print("Part 1: ", highest_y)
print("Part 2: ", len(velocities))

