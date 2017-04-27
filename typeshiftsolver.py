import enchant

def main():

        #Initialize dictionary
        dictionary = enchant.Dict("en_US")

	# Tiles, by column, in typeshift puzzle
	tiles = ['mlad','arem','cnio','avtn','uig','esrn','egtr']
	#tiles = ['suc','etnl','ouel','plas','iurp','nae','dgrl']
        #^ This took 1 hr 21 min 9.56 sec. 15 words found.

	#Print and analyze columns
	columnLengths = []
	print('Columns')
	for column in tiles:
		print(column)
		columnLengths.append(len(column))

	# Generate every combination of tiles
		#Find number of possible combinations
	totalCombinations = 1
	for length in columnLengths:
		totalCombinations *= length
	print 'Total combinations: ',totalCombinations

    	#Now generate every possible combo

	words = [] #list of all combos
	comboIndex = [0]*len(tiles) #initialize combo counter

	for n in range(totalCombinations):
		word = ''
		for i in range(len(tiles)):
			word = word+tiles[i][comboIndex[i]]

		words.append(word)

		comboIndex = step(comboIndex,columnLengths)

	#Check words against dictionary (enchant)
        foundWords = 0
        for word in words:
            if dictionary.check(word):
                print word
                foundWords += 1

        print 'Found',foundWords,'words'
        return
        # End of program

def step(ndx,lens):
	for i in range(len(ndx)-1,-1,-1):
		ndx[i] += 1
		if ndx[i] >= lens[i]:
			ndx[i] = 0
		else:
			break
	return ndx

if __name__ == "__main__":
    main()
