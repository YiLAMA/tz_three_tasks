# tz_three_tasks
### Task 1: (Выполнен) 

Дан массив (список) чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000. 

- Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули). 
- Указать, какова сложность вашего алгоритма. 

Например: 
```
print(task("111111111111111111111111100000000"))
```
**>> OUT: 25** 

### Task 2: (Выполнен)

Получить с русской википедии список всех животных ([Категория:Животные по алфавиту](https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83 "Категория:Животные по алфавиту")) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
```
А: 642
Б: 412
В: ...
```
### Task 3: (Выполнен)

В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): 

— lesson – начало и конец урока;  

— pupil – интервалы присутствия ученика;  

— tutor – интервалы присутствия учителя.  

Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока. 

Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах). 

Например:
```
print(appearance({ 
  'lesson': [1594663200, 1594666800], 
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
})) 
```
**>> OUT: 3117** 

### Task 3. Будет плюсом: WEB API с единственным endpoint’ом для вызова этой функции. (ВЫПОЛНЕН)
- с помощью fastapi[all]. 
- Результат работы можно увидеть в папке task3/screenshots
