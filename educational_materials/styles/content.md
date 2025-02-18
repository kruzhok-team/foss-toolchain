# Оформление кода

Если мы хотим создать полезную библиотеку, мы должны позаботиться об оформлении кода, чтобы его было удобно читать. Для больших проектов с активным сообществом справедливо утверждение, что код больше читают, чем пишут. И если мы хотим участвовать в таком сообществе, нужно не только производить фичи, но и хорошо их оформлять. Хорошо — это значит общепринятым способом, чтобы другой разработчик не тратил время на понимание того, что вы почему-то решили назвать переменную так, как обычно называют класс. Есть интуитивно понятные правила оформления кода, например, с использованием отступов. Но существуют не такие очевидные, например, где мы должны переносить строку, [до или после знака оператора](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator):

```python 
#wrong
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

#correct    
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

Можно думать о стиле как о минимально необходимом наборе всех возможностей языка программирования по написанию и оформлению кода: даже если мы можем так написать, мы не будем — в угоду читаемости. Соблюдение стиля не всегда приводит к меньшему количеству кода. Мы можем обратиться к дзену Python и увидим, что там нет строчки про количество кода, поэтому лучше получить более читаемый, явный и простой код, чем короткий, но сложный, в котором происходит что-то неявное. 

```python
import this 

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Базовые практики

### Используйте отступы

Одно из основных правил хорошего стиля программирования (code style) заключается в том, что разные уровни вложенности стоит выделять при помощи отступов, используя знаки пробела или табуляции. **Работая с кодом в рамках одного файла, стоит использовать что-то одно: или пробелы, или табуляцию**. 
Если вы попробуете использовать и то, и другое, набирая код программы на Python, то интерпретатор выдаст вам сообщение об ошибке. В других языках программирования такая ситуация не вызовет ошибку синтаксиса, однако читать код с отступами приятнее, он легче и быстрее воспринимается разработчиком. Еще больше информации о стиле программирования можно узнать из документа [pep8](https://peps.python.org/pep-0008/). В нем множество рекомендаций по оформлению кода на языке Python.

Код без отступов:

([код](/projects/styles/no_indented_code.cpp)):

```c++
#include <iostream>

#define DEFINE_NAME true

int main() 
{   
//not indented code    
char* name;
if(DEFINE_NAME) 
{
name = (char*) "Name";
std::cout << "Hello, " << name << "!";    
} 
else 
{
std::cout << "Hello World!";    
}
return 0;   
}
```

Код с отступами:

([код](/projects/styles/indented_code.cpp)):

```c++
#include <iostream>

#define DEFINE_NAME true

int main ()
{
  char *name;
  if (DEFINE_NAME)
    {
      name = (char *) "Name";
      std::cout << "Hello, " << name << "!";
    }
  else
    {
      std::cout << "Hello World!";
    }
  return 0;
}

```

В Python также есть ситуации, когда отступы не будут приводить к ошибке, например, при вызове функции, название и аргументы которой не помещаются в максимальную длину строки и должны быть перенесены на следующую строку.

```python 
#ok 
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

#ok 
foo = long_function_name(
    var_one, var_two, var_three, var_four
)

#not_so_buity
foo = long_function_name(var_one, var_two,
           var_three, var_four)
```

Оба варианта валидны с точки зрения интерпретатора, но первый более читаем. В [разных](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator) ситуациях отступы используются по-разному. Если чувствуете, что участок кода сложен при оформлении, обратитесь к руководству по стилю. 

### Соблюдайте принятую длину строки

В разных языках программирования и в разных проектах может быть принята разная максимальная длина строки. Когда я работал над проектом на Java, мы использовали длину строки 120 символов. В Python принято вмещать код на каждой строке в [79 символов](https://peps.python.org/pep-0008/#maximum-line-length), а комментарии в 72 символа. Отчасти это историческое ограничение, связанное с тем, что раньше были маленькие экраны. Но даже с появлением широкоформатных экранов от этого элемента форматирования не стали отказываться, так как человеку проще воспринимать более узкие колонки текста. Во многих изданиях принято оформлять текст в виде нескольких колонок на одной странице, хотя ничто не мешает занять всю ширину страницы. Также такой подход позволяет разделить экран ноутбука на две области и быть уверенными, что код войдет по ширине в обе, и шрифт не будет слишком мелким. Не заставляйте своих коллег скролить горизонтально, это не круто.

Существуют разные способы разбить длинную строку на несколько коротких. Они будут зависеть от языка программирования и от конкретного участка кода, который нужно перенести на другую строку. 

```python
if super_long_condition_variable == True and another_condition_with_yet_longer_name == False:
    pass
    # do stuff here
```

Просто перенести второе условие на новую строку нельзя, будет ошибка:

```python
if super_long_condition_variable == True and
   another_condition_with_yet_longer_name == False:
    pass
    # do stuff here

...
    if super_long_condition_variable == True and
                                                 ^
SyntaxError: invalid syntax
```

Можно окружить условие скобками. Скобки имеют более высокий приоритет, чем перенос, поэтому пример внизу выполнится корректно

```python
if (super_long_condition_variable == True and 
    another_condition_with_yet_longer_name == False):
    pass
    # do stuff here
```

Можно использовать явный способ сказать интерпретатору, что строка ниже является продолжением текущей строки:

```python
if super_long_condition_variable == True and \
   another_condition_with_yet_longer_name == False:
    pass
    # do stuff here
```
В математических выражениях удобнее использовать скобки:

```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

Так же, как и при вызове функции.

```python
long_function_name(var_one, var_two, var_three, var_four,
                   var_six, var_seven, var_eight)
```

Разные инструменты используют различную длину строки по умолчанию, но ее всегда можно настроить при запуске форматирования. Ниже пример с [black](https://github.com/psf/black):

<pre><code class="shell">
black --line-length 80 example.py
</code></pre>

### Используйте фигурные скобки правильно

В С++ и в других языках, которые используют фигурные скобки для выделение блоков кода, мы можем не писать фигурные скобки у условного оператора или оператора цикла. 

```C++
int age;
//get age from user
if(age >= 18) 
    allow_18plus_content();
else 
    disable_18plus_content();
```

Но лучше всегда их использовать, даже если вы полностью уверены, что в тело условия больше не будет добавлено ни одной строчки. Опять же, использование единого оформления позволит не отвлекаться и читать код быстрее. 

```C++
int age;
//get age from user
if(age >= 18) 
{
    allow_18plus_content();
}
else 
{
    disable_18plus_content();
}
```

Есть также альтернативное оформление, которое, на мой взгляд, выглядит более приятно при условии использования отступов. Уточните, какой из этих способов принят в команде, к которой вы подключаетесь. Но скобки должны быть всегда.

```C++
int age;
//get age from user
if(age >= 18) {
    allow_18plus_content();
} else {
    disable_18plus_content();
}
```

### Именуйте объекты правильно

Среди начинающих программистов и своих студентов я часто встречаю именование переменных либо одним ничего не значащим символом, любо транслитом. 

```python
def srednee(znacheniya):
    return sum(znacheniya) / len(znacheniya)
```

Как первое, так и второе — плохо. Именование с использованием транслита не позволит другому разработчику понять, что это за функция и что она делает. Еще одна частая проблема, которая встречается при именовании объектов, — сохранение контекста, который использовался при разработке. Например, мы работаем с датчиком, который предоставляет температуру (`temperature`) и давление (`pressure`). Мы хотим как-то обработать данные, например, найти среднее значение. Мы начинаем разработку и выбираем использовать температуру, чтобы проверять нашу работу. Мы правильно пишем название функции, а аргументом передаем список снятых значений температуры. Вроде бы все нормально. 

```python
def average(temperature):
    return sum(temperature) / len(temperature)

vals = measure_temperature()
average_temperature = average(vals)
```

Мы протестировали функцию и довольны ее работой, и теперь готовы применить ее к показаниям давления. И все... работает. Мы счастливы и коммитим свою работу. А разработчик, который будет потом разбираться в нашем коде, долго не сможет понять, почему температура ведет себя как давление.

```python
vals = measure_pressure()
average_pressure = average(vals)
```

Используйте несколько слов там, где это нужно. Например, мы могли просто назвать функцию `pressure()`.  И что это значит, "давление"? Измерить, прочитать из файла, забрать из базы данных, что я делаю с давлением? Тот вариант, который использовали мы, `measure_pressure()`, сразу даст понять, что это функция измерения давления, и скорее всего она работает с датчиком, а не получает давление каким-то другим способом. Здесь можно прокомментировать, что непонятно, что эта функция дает ряд значений, а не одно. Мы можем согласиться с этим и добавить эту информацию к названию функции, или сделать это через обязательные аргументы.
Существуют два основных способа именования переменных и функций: через подчеркивания (`measure_pressure`) и CamelCase (`measurePressure`). На мой взгляд, через подчеркивание удобнее, так как мы используем название классов с заглавными буквами (`PressureSensor`), и при беглом чтении разница в одной заглавной (для классов) или строчной (для переменных и функций) менее заметна, чем при использовании подчеркиваний.
При выборе имени для переменной используйте существительные, а для функции — глагол.

### Придерживаться определенного подхода

Этот пункт не относится напрямую к стилю кода и не является строгим требованием. Код состоит из определенных конструкций, и неплохая идея — пользоваться одним подходом для написания одной и той же функциональности. Например, если нам нужно открыть файл, мы можем сделать это несколькими способами:


```python
with open(filename) as f:
    #do something
```

или

```python 
f = open(filename)
#do something
f.close()
```

Это простой пример, и есть соглашение о том, что конструкция с `with` лучше. Но в других ситуациях, когда нет устоявшегося способа написать участок кода, вам придется приходить к этому внутри команды. То же самое касается и подходов к программированию. Например, Python позволяет использовать основные парадигмы программирования: объектно-ориентированную, процедурную, функциональную и императивную. Мы можем смешивать их в рамках одной программы, и это не будет ошибкой. Есть решения, где использование другого подхода оправдано: все так делают, и решение более красивое и явное, чем при использовании другого подхода. Однако использование другого подхода только ради того, чтобы его использовать, не будет хорошей идеей и ухудшит читаемость кода.

### Избегайте вложенности (Flat is better than nested)

Этот пункт взять из дзена Python, и ему можно легко дать количественную оценку — уровни вложенности можно посчитать. Возьмем код ниже: 

([код](/projects/styles/nested.py)):

```python 
#nested
def foo(a, b, c):
    if a > 5:
        if b > 10:
            if c != 6: 
                return a + b + c
    return None
```

И уберем вложенность:

([код](/projects/styles/flat.py)):

```python
def foo(a, b, c):
    if a <= 5:
        return None
    if b <= 10:
        return None
    if c != 6: 
        return None
    return a + b + c
```


Задание: попробуйте прогнать код с вложенностью через autopep8 и проверьте, что произойдет. Как думаете, почему так?


### Не перегружайте код (Sparse is better than dense)

Хотя мы должны вмещать код в 8 строк, мы можем написать очень насыщенный код. Код ниже заставить разработчика остановиться и потратить какое-то время, чтобы разобраться в нем, если ему нужно что-то поправить или реализовать подобный функционал у себя.

([код](/projects/styles/dense.py)):

```python 
capacity = [(j * 8, 256**j-1) for j in (1 << i for i in range(4))]
print("\n".join("%i bits can store number up to %i" % bc for bc in capacity))
```

```
8 bits can store number up to 255
16 bits can store number up to 65535
32 bits can store number up to 4294967295
64 bits can store number up to 18446744073709551615
```

Написав больше кода, мы можем уменьшить время, которое разработчик тратит на изучение этого участка.

([код](/projects/styles/sparse.py)):

```python
capacity = list()
for i in range(4):
    j = 1 << i
    bits = j * 8
    max_val = 256**j - 1
    capacity.append((bits , max_val))

for bits, max_val in capacity:
    print("%i bits can store number up to %i" % (bits, max_val))
```

### Используйте принятый регистр для разных сущностей

Название классов в CamelCase.

```python
# MarketItem in CamelCase
class MarketItem(str): 
    pass
```

Название пременных и функций офомляем в snake_case

```python
# order_items, item and amount in snake_case
def order_items(item, amount):
    for _ in range(amount):
        # order item here
        pass
```


### Имена переменных явлюятся полными и информативными

Используйте имена, которые дают представления о том, что этот объект значит в контескте поекта:

```python
#bad naming 
for m in mm:
    if m == "January":
       d = 31

#good 
for month in months:
    if month == "January":
       days_in_month = 31

```

В зависимости от контекста можно исользовать более простые имена, например days вместо days_in_month:

```python
for month in months:
    if month == "January":
       days = 31
```

### Не обанывайте

Имена переменых должны соответствовать смыслу зранящихся в них значений:

```python
days_in_month = 0
year = 2025
for month in months:
    if month == "January":
       days_in_month += 31
    ...
    if month == "December":
       days_in_month += 31
print(f"There is {days_in_month} days in {year} year")
```

### Используйте f-cтроки

Предпочтительный способ форматирования вывода f-string:

```python
print(f"There is {days_in_month} days in {year} year")
```

Вместо

```python
print("There is {} days in {} year".format(days_in_month, year))
```

### Аннотация типов

Присутствует аннотация типов для параметров и выходного значения функции

```python
# without annotation
def check_visible_satellites(site, sats, epoch):
    observed = dict()
    for sat in sats:
       observed[sat] = is_observed(site, sat)
    return observed

# with annotation
def check_visible_satellites(
   site: str, 
   sats: list[str],
   epoch: datetime.datetime
) -> dict[str, bool]:
    observed = dict()
    for sat in sats:
       observed[sat] = is_observed(site, sat)
    return observed
```

### Используйте свои объекты

Как видно из примеров выше мы использовали тип str для обозначения как спутника так и приемника (site). Из контекста понятно что dict[str, bool] содержит в качестве ключей спутники, однако это понятно не всегда, *для того, чтобы можно было быстрее понять структуру, мы можем делать классы* даже если там храниться таже информаци, что и в одной переменной.

```python
class Satellite():
    def __init__(self, name: str):
        self.name = name

class Site():
    def __init__(self, name: str, lat: float, lon: float):
        self.name = name
        self.lat = lat
        self.lon = lon

def check_visible_satellites(
   site: Site, 
   sats: list[Satellite],
   epoch: datetime.datetime
) -> dict[Satellite, bool]:
    observed = dict()
    for sat in sats:
       observed[sat] = is_observed(site, sat)
    return observed
```

### Группируйте константы

Использовать перечисления чтобы хранить константы, которые относятся к одной группе. 

```python
from enum import Enum

class GNSS(Enum):
    GPS = "GPS"
    GLO = "GLONASS"
    GAL = "Galileo"
    BDS = "BeiDou"
```

Использование перечислений сохранит время разработчику, чтобы выяснить, какие именно значения может принимать тот или иной аргумент.

```python
# without enumerations
def is_belong_to_gnss(
   site: Site, 
   gnss: str
) -> bool:
    if sat.name[0] == "G" and gnss == "gps":
        return true:
    elif: 
        ....
        # other systems here
    return false

# fails since "GPS" is passed instead of "gps"
is_belong_to_gnss(Satellite("G03"), "GPS")
```

Будет ошибка из-за того, что передано `GPS` вместо `gps` 

```python

# with enumerations
def is_belong_to_gnss(
   site: Site, 
   gnss: GNSS
) -> bool:
    if sat.name[0] == "G" and gnss == GNSS.GPS:
        return true:
    elif: 
        ....
        # other systems here
    return false

is_belong_to_gnss(Satellite("G03"), GNSS.GPS)
```

Так же можете использовать свои классы:


```python
from enum import Enum

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point(%r, %r)' % (self.x, self.y)

class Corner(Enum):
    BottomLeft = Point(0, 0)
    TopLeft = Point(0, 100)
    TopRight = Point(100, 100)
    BottmRight = Point(100, 0)
```

### Название функций должно начинаться с глагола

```python
# bad
def addition(a: float, b: float):
    return a + b 

# very bad
def operation(a: float, b: float):
    return a + b

# good 
def add(a: float, b: float):
    return a + b
```

### Single responsibility

Одна *функция должна делать одно специфичное действие* , т.е. функцию read_and_parse_data() должна быть разбита на две и написано какие именно данные она читает read_data() и разбивает parse_data():

```python
from pathlib import Path

def read_data(filename: Path) -> list[str]:
    with open(filename, 'r') as file:
        return file.readlines()

def parse_data(data: list[str]) -> dict[str, int]:
    parsed_data = {}
    for line in data:
        key, value = line.strip().split(',')
        parsed_data[key] = int(value)
    return parsed_data
```

### Используйте кастомные исключения

При необходимости используйте [кастомные исключения](https://realpython.com/python-raise-exception/#raising-built-in-exceptions). Название ошибки должно отсылать к месту где произошла ошибка.  При этом следует помнить что не несколько ситуаций может быть описано одним классом, а детали можно описать в сообщении (например pytest [позволяет разделять](https://docs.pytest.org/en/8.0.x/how-to/assert.html#matching-exception-messages) ошибки по сообщению). Ниже пример того как один класс ошибок используется с разными сообщениями.

```python
# grades.py

class GradeValueError(Exception):
    pass

def calculate_average_grade(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            raise GradeValueError(
                "grade values must be between 0 and 100 inclusive"
            )
        if grade - int(grade) != 0:
            raise GradeValueError(
                "grade must be integer"
            )
        total += grade
        count += 1
    return round(total / count, 2)
```

### Используйте правильные объекты

Для хранения сущностей используются классы, которые предназначены для этого. Ниже приведен пример, того как для пути файла можно использовать строку, но удобнее использовать Path из pathlib.

```python

#could be better
def read_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.readlines()

#good
from pathlib import Path
def read_data(filename: Path) -> list[str]:
    with open(filename, 'r') as file:
        return file.readlines()
```

## Автоматизируйте то, что можно автоматизировать

Форматирование кода соответствует [black](https://github.com/psf/black). Можно воспользоваться автоматическим [инструментом](https://semakin.dev/2020/05/black/) для форматирования или посмотреть как будет выглядеть форматирование с помощью онлайн [редактора](https://black.vercel.app/?version=stable). Так же существуют [расширения для VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) и PyCharm.


## Выводы

Придерживаться стиля нужно для того, чтобы писать код понятно. Хороший стиль помогает быстро сориентироваться в коде и найти тот участок, за которым вы пришли в этот модуль. Часть работы по оформлению кода можно делегировать автоматическим средствам, таким как `autopep8` или `black`. Про другую часть придется помнить и писать код с учетом этих знаний. Стиль — это не про то, чтобы писать меньше кода. Иногда (редко) вам будет казаться, что придерживаться стиля контринтуитивно, а получивший код некрасив. Но если так пишет большинство разработчиков — придерживайтесь рекомендаций, со временем вы привыкнете. Вы не сможете начать хорошо оформлять код без практики: пишите, а самое главное — читайте чужой код, чтобы понять, как пишут ваши коллеги. 

