#Користувач вводить температуру у форматі `00.00 Х -> Y`, де `Х` та `Y` позначають одиниці вимірювання і належать множині `{ C, F, K }`.
# Напишіть функцію, що переводить температуру з одиниць `Х` у одиниці `Y`. Виведіть результат.
#У випадку помилкового вводу виведіть повідомлення про помилку.
#С = К - 273.15 = (F - 32)/(1.8),
#F = 1.8 K - 459.67
#(Кельвіни не можуть бути менше 0.)




def fah2cel(fah):
    cel = 5*(fah - 32) / 9
    return cel


def cel2fah(cel):
    fah = (9/5 * cel) +32
    return fah




