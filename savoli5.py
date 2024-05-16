adad = input[list] 
min_adad = adad.index(min(adad))  
max_adad = adad.index(max(adad))  

adad[min_index], adad[max_index] = adad[max_index], adad[min_index]

print(adad)  
#numbers = [3, 4, 5, 2, 1]  # Ин рӯйхати шумо аст
#min_index = numbers.index(min(numbers))  # Индекси элементи минималӣ
#max_index = numbers.index(max(numbers))  # Индекси элементи максималӣ

# Иваз кардани элементҳои минималӣ ва максималӣ
#numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

#print(numbers)  # Рӯйхати навро чоп мекунем
