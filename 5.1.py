age = int(input('Введите свой возраст: '))
height = float(input('Введите свой рост: '))
weight = float(input('Введите свой вес: '))
bmi = weight / height ** 2
bmi = round(bmi, 2)
if bmi < 18.5:
    description = "недостаточной массой тела."
elif bmi < 25:
    description = "нормальной массой тела."
elif bmi < 30:
    description = "избыточной массой тела."  
else:
    description = "ожирением."
print("bmi=", bmi, "Вы относитесь к группе людей с", description)
