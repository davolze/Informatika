numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbersNEW = numbers[:numbers.index(None)]+numbers[numbers.index(None)+1:]
midnum = sum(numbersNEW)/len(numbers)
listik = [midnum]
numbersNEW = numbers[:numbers.index(None)]+listik + numbers[numbers.index(None)+1:]
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbersNEW)
