# a, b, c = map(int, input().split())
# # print(a, b, c, b ^ 2, pow(b, 2))
# D = pow(b, 2) - 4 * a * c
# # print(D)
# if D > 0:
#     x1 = (-b + pow(D, 0.5)) / 2 / a
#     x2 = (-b - pow(D, 0.5)) / 2 / a
#     print('Уравнение имеет корни', x1, 'и', x2)
# elif D == 0:
#     print('Уравнение имеет корень', -b / 2 / a)
# else:
#     print('Уравнение корней не имеет')

sp = list(map(int, input().split()))
pp = []
for i in range(len(sp)):
    a = [bin(sp[i])[2:].count('1'), sp[i]]
    pp.append(a)
print(sp)
print(pp)
pp = sorted(pp)
print(pp)
op = [x[1] for x in pp]
print(op)
# ИЛИ просто
print([x[1] for x in pp])