# TODO Найдите количество книг, которое можно разместить на дискете
page = 100
line = 50
symb = 25
weight = 4
maxweight = 1.44*1024*1024
print("Количество книг, помещающихся на дискету:", int(maxweight//(page*line*symb*weight)))
