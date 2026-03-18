numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25] #исходная строка
numbersNEW = numbers[:numbers.index(None)]+numbers[numbers.index(None)+1:] #срезает строку до None и после None
midnum = sum(numbersNEW)/len(numbers) #вычисляет сречнее значение
listik = [midnum] #превращает нужное число в список
numbersNEW = numbers[:numbers.index(None)]+listik + numbers[numbers.index(None)+1:] #вставляет среднее арифметическое на место None по срезам

print("Измененный список:", numbersNEW)
