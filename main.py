##############################
# Program to address bias in AI datasets
##############################

# Descriptive analysis of original dataset before mitigation
originalData = open("OriginalDatasetUrology.csv","r")
augmentedData = open("AugmentedDataset.csv","w")
originalFemaleCount = 0
originalMaleCount = 0

for inputLine in originalData:
		augmentedData.write(inputLine)
		if inputLine.find(' female ') != -1:
			originalFemaleCount+=1
		if inputLine.find(' male ') != -1:
			originalMaleCount+=1
print("Original Female Count: " + str(originalFemaleCount))
print("Original Male Count: " + str(originalMaleCount))
augmentedData.write("\n")
augmentedData.close()
originalData.close()

# Bias mitigation
originalData = open("OriginalDatasetUrology.csv","r")
augmentedData = open("AugmentedDataset.csv","a")
for inputLine in originalData:
	outputLine = ""
	if inputLine.find(' female ') != -1:
		outputLine = inputLine.replace(" female "," male ")
	if inputLine.find(' male ') != -1:
		outputLine = inputLine.replace(" male "," female ")
	augmentedData.write(outputLine)
augmentedData.close()
originalData.close()

# Descriptive analysis of augmented dataset (after)
augmentedData = open("AugmentedDataset.csv","r")
augmentedFemaleCount = 0
augmentedMaleCount = 0

for inputLine in augmentedData:
		if inputLine.find(' female ') != -1:
			augmentedFemaleCount+=1
		if inputLine.find(' male ') != -1:
			augmentedMaleCount+=1
print("\nAugmented Female Count: " + str(augmentedFemaleCount))
print("Augmented Male Count: " + str(augmentedMaleCount))

##############################







print("\n")
