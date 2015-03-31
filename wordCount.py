myList = ['great', 'good', 'adventure', 'the', 'while']

myFile = open('brazilWildBook.txt')
contents = myFile.read().lower()
myFile.close()

print "Number of times the word 'great' appears in the file:", contents.count('great')
print "Number of times the word 'good' appears in the file:", contents.count('good')
print "Number of times the word 'adventure' appears in the file:", contents.count('adventure')
print "Number of times the word 'the' appears in the file:", contents.count('the')
print "Number of times the word 'while' appears in the file:", contents.count('while')
