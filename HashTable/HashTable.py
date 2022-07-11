class Hashtable():
    def __init__(self,size):
        self.linear = [None for i in range(size)]
        self.quadratic = [None for i in range(size)]
        self.chain = [None for i in range(size)]
        self.size = size
    
    def hashfunction(self,x):
        return x

    def insert(self,num):
        self.insertlinear(num)
        try: self.insertquadratic(num)
        except: print("%s Cannot be Inserted"%num)
        self.seperatechaining(num)
    
    def insertlinear(self,num,linear = 0):
        h = self.hashfunction(num)
        index = (h+linear)%self.size

        if self.linear[index] is None:
            self.linear[index] = num
        else:
            self.insertlinear(num,linear+1)
    
    def insertquadratic(self,num,quad = 0):
        h = self.hashfunction(num)
        index = (h+(quad**2))%self.size

        if self.quadratic[index] is None:
            self.quadratic[index] = num
        else:
            self.insertquadratic(num,quad+1)
    
    def seperatechaining(self,num):
        h = self.hashfunction(num)
        index = h%self.size

        if self.chain[index] is None:
            self.chain[index] = [num]
        else:
            self.chain[index].append(num)
    
    def __str__(self):
        return "\nLinear Probing: " + str(self.linear) + "\nQuadratic Prbing: " + str(self.quadratic) + "\nSeperate Chain:\n" + "\n".join([str(i) + " -> " + str(self.chain[i]) for i in range(self.size)])
    
def main():
    N = int(input())
    print("Size of the HashTable: %s"%N)
    H = Hashtable(N)
    print("The %s Elements that is added are:"%N)
    for i in [int(i) for i in input().split(" ")]: 
        H.insert(i)
        print("%s "%i,end = " ")
    print(H)


if __name__ == "__main__":
    main()