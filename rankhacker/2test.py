if __name__ == '__main__':
    nest = []
    i = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nest[i].append(name, score)
        i += 1
    print(nest)
    for i in nest:
    	print(i)
    	for j in i[1]:
    		print(j)