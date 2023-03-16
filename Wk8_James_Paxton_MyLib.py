#MyLib

class calc():
    def checknum(self,lb,n,ub):
        return lb < n < ub

    def add(self,n1,n2):
        return n1 + n2

    def subtract(self,n1,n2):
        return n1 - n2

    def multiply(self,n1,n2):
        return n1 * n2

    def divide(self,n1,n2):
        return n1 / n2

    def scalc(self,p1):
        istring = p1.split(",")
        num1 = float(istring[0])
        num2 = float(istring[1])
        if istring[2] == "+":
            return num1 + num2
        elif istring[2] == "-":
            return num1 - num2
        elif istring[2] == "*":
            return num1 * num2
        elif istring[2] == "/":
            return num1 / num2

    def allInOne(self,n1,n2):
        results = {}
        results["add"] = n1+n2
        results["sub"] = n1-n2
        results["mult"] = n1*n2
        results["div"] = n1/n2
        return results

    def main(self):
        option = -1
        while option != '8':
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            menu = """
            1)  Add two numbers
            2)  Mult two number
            3)  Divide
            4)  Subtract
            5)  All in one
            6)  Write file
            7)  Read file
            8)  Exit
            Your option: """
            option = input(menu)
            res = self.allInOne(n1, n2)
            if(option == '1'):
                print("{} + {} = {}".format(n1, n2, res['add']))
            elif(option == '2'):
                print("{} * {} = {}".format(n1, n2, res['mult']))
            elif(option == '3'):
                print("{} / {} = {}".format(n1, n2, res['div']))
            elif(option == '4'):
                print("{} - {} = {}".format(n1, n2, res['sub']))
            elif(option == '5'):
                print("{} + {} = {}".format(n1, n2, res['add']))
                print("{} - {} = {}".format(n1, n2, res['sub']))
                print("{} * {} = {}".format(n1, n2, res['mult']))
                print("{} / {} = {}".format(n1, n2, res['div']))
            #This lets you name a file to the problem you just entered
            elif(option == '6'):
                res = self.allInOne(n1,n2)
                wrfile.writeToFile(n1,n2,res)
            #This lets you recall a file you named before and see what you've entered
            elif(option == '7'):
                wrfile.readFromFile()                

class wrfile:
	
	# This is to write into file
	def writeToFile(num1, num2, dictionary):
		filename = input("Enter text filename to write: ")
		File = open(filename, 'w')
		File.write(str(num1)+' + '+str(num2)+" = "+str(dictionary['add'])+'\n')
		File.write(str(num1)+' - '+str(num2)+" = "+str(dictionary['sub'])+'\n')
		File.write(str(num1)+' * '+str(num2)+" = "+str(dictionary['mult'])+'\n')
		File.write(str(num1)+' / '+str(num2)+" = "+str(dictionary['div'])+'\n')
		File.close()
		print("Successfully written!")
	
	
	# This is to get data from file
	def readFromFile():
		filename = input("Enter text filename to read: ")
		try:
			File = open(filename, 'r')
		except FileNotFoundError:
			print(filename,"not found!")
		else:
			for line in File:
				line = line.strip()
				print(line)
			File.close()
