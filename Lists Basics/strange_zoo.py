tail = input()
body = input()
head = input()

strange_meerkat = [tail, body, head]

strange_meerkat[0], strange_meerkat[2] = strange_meerkat[2], strange_meerkat[0]

print(strange_meerkat)