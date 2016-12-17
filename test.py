d = {}
sz = 8
for i in range(sz):
    d[chr(97+i)] = i
    print("<%s,%d> added"%(chr(97+i), i))

print("\nKeys:")
print(''.join(d.keys()))
print(''.join(d.keys()))
