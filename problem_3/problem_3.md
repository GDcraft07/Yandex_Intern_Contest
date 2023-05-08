# Условие

Кузя изучает биографии самых известных трейдеров на бирже. Недавно Кузя прочитал историю о том, как, совершив всего четыре сделки (две покупки и две продажи) акций на бирже, трейдер смог превратить один рубль в целое состояние.
Кузя лучше всех знает, что такой удачи не бывает, а значит у трейдера была инсайдерская информация о ценах на ближайшие дни.
«Да если бы у меня была инсайдерская информация, я бы еще больше денег за четыре сделки получил!» — заявил Кузя перед своим преподавателем экономики. Преподаватель экономики не растерялся и выдал Кузе данные о ценах акций фирмы Тындекс за тот период.
Для простоты вычислений преподаватель предложил считать, что можно покупать и продавать любую дробную часть акции. Например, если акция стоит 
2
 рубля, а у вас в наличии 
3
 рубля, то вы можете купить 
1
.
5
 акции.
Преподаватель ожидает, что Кузя вычислит наибольшее количество денег, которые можно получить из 
1
 рубля на старте, совершив не более четырех сделок.
Кузя резко вспомнил о множестве других очень важных дел, поэтому он просит вас, как знатока большинства промокодов и акций в супермаркетах, вычислить оптимальные дни для сделок на основе исторических данных.

# Формат ввода
В первой строке расположено единственное целое число 
N
(
1
≤
N
≤
3
⋅
1
0
5
)
 — количество дней в исторических данных.
Вторая строка содержит 
N
 целых чисел через пробел 
p
i
(
1
≤
p
i
≤
1
0
4
)
 — цена одной акции Тындекса в рублях в 
i
-й день.

# Формат вывода
В первой строке выведите одно целое число 
K
(
0
≤
K
≤
2
)
 — количество пар сделок «покупка — продажа» в оптимальной стратегии торговли, приводящей к наибольшему количеству денег из 
1
 рубля на старте.
Следующие 
K
 строк должны содержать по два целых числа через пробел 
b
i
s
i
(
1
≤
b
i
<
s
i
≤
N
)
 — дни покупки и продажи акций в 
i
-й паре сделок.
Обратите внимание, что вы можете не совершать сделок вовсе или совершить только одну пару сделок.
Если вы считаете оптимальным совершить две пары сделок, то выведенные дни сделок должны следовать в общем хронологическом порядке, то есть 
b
1
<
s
1
<
b
2
<
s
2
.
Если оптимальных ответов, содержащих не более четырех сделок, несколько, выведите любой из оптимальных.