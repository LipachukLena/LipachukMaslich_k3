def key(f,e):
  d=1
  while (d*e)%f != 1:
    d += 1
  return d
p = 61
q = 67
print("2 простых числа: ", p, q)
mod = p*q
print("Модуль: ", mod)
f = (p-1)*(q-1)
print("Функция эйлера: ", f)
#простое число меньшее функции эйлера!
e = 7
print("Экспонента: ",e)
print("Открытый ключ: ", e, mod)
d = key(f,e)
print("Cекретный ключ: ", d, mod)
text = int(input("Введите число: "))
text1 = (text**e)%mod
print("Зашифрованный текст: ", text1)
text2=(text1**d)%mod
print("Расшифрованный текст: ",text2)
