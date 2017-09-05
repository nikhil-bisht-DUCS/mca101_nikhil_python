num_A = int(input("Enter A: "))
num_B = int(input("Enter B: "))

num_A += num_B
num_B = num_A - num_B
num_A -= num_B

print("A ---> %d\tB ---> %d" % (num_A, num_B))
