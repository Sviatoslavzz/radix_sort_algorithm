## Реализация алгоритма поразрядной сортировки
Поразрядная сортировка является одним из видов сортировки, которые работают практически за линейное от размера сортируемого массива время. 
Такая скорость достигается за счет того, что эта сортировка использует внутреннюю структуру сортируемых объектов.  

### Алгоритм
Будем, для простоты, в этой задаче рассматривать строки из цифр от 0 до 9. Для каждой цифры создается «корзина» («bucket»), 
после чего строки si распределяются по «корзинам» в соответствии с i-ой цифрой с конца. 
Строки, у которых i-ая с конца цифра равна j попадают в j-ую корзину (например, строка 123 на первой фазе попадет в третью корзину, 
на второй — во вторую, на третьей — в первую). После этого элементы извлекаются из корзин в порядке увеличения номера корзины. 
Таким образом, после первой фазы строки отсортированы по последней цифре, после двух фаз — по двум последним, ..., после m фаз — по всем. 
При важно, чтобы элементы в корзинах сохраняли тот же порядок, что и в исходном массиве (до начала этой фазы). 
Например, если массив до первой фазы имеет вид: 111, 112, 211, 311, то элементы по корзинам распределятся следующим образом: 
в первой корзине будет. 111, 211, 311, а второй: 112.

### Формат ввода
Первая строка входного файла содержит целое число n (1 ≤ n ≤ 1000). Последующие n строк содержат каждая по одной строке s<sub>i</sub>. 
Длины всех s<sub>i</sub>, одинаковы и не превосходят 20. Все s<sub>i</sub> состоят только из цифр от 0 до 9.

### Формат вывода
Выводится исходный массив строк, состояние «корзин» после распределения элементов по ним для каждой фазы и отсортированный массив.