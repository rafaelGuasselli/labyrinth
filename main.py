from map import Level

h, w = map(int, input().split())
map = Level((h, w))
print(map.render())