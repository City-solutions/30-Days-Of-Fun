class Person:

	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, idNumber, score):
        self.firstName= first_name
        self.lastName = last_name
        self.idNumber= idNumber
        self.score = score
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here   
    def calculate(self):
        score = 0
        count = 0
        for i in range(len(self.scores)):
            score += self.scores[i]
            count += 1   
        avgScores = score / count
        
        if avgScores in range(90, 101):
            grade = 'O'
        
        elif avgScores in range(80, 91):
            grade = 'E'
        
        elif avgScores in range(70, 81):
            grade = 'A'
        
        elif avgScores in range(55, 71):
            grade = 'P'
            
        elif avgScores in range(40, 56):
            grade = 'D'
            
        elif avgScores in range(0, 41):
            grade = 'T'
            
        else:
            grade = 'Invalid grade'
            
        return grade
        
line = input().split()