### Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
```bash
cut -d: -f1 /etc/passwd | sort
```
![img_1.png](img_1.png)
### Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:
![img.png](img.png)
```bash
cat /etc/protocols | sort -nrk2 | head -n 5 | awk '{print $2, $1}'
```
![img_4.png](img_4.png)
### Задача 3
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):
![img_2.png](img_2.png)
Перед отправкой решения проверьте его в ShellCheck на предупреждения.
```bash
./new_file.sh AAAAAAAAAAAAAAAAA

#!/bin/bash
string=$1
size=${#string}
echo -n "+"
for ((i=0;i<size + 2;i++))
do
echo -n "-"
done
echo "+"
echo "| $string |"
echo -n "+"
for ((i=0;i<size + 2;i++))
do
echo -n "-"
done
echo "+"
```
![img_5.png](img_5.png)
### Задача 4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:
![img_3.png](img_3.png)
```bash
grep -o '\b[a-zA-Z_][a-zA-Z0-9_]*\b' main.cpp | sort | uniq

```
![img_10.png](img_10.png)
### Задача 5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

__./reg banner__

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.
```bash
#!/bin/bash

chmod +x "$1"
sudo cp "$1" /usr/local/bin/
```
### Задача 6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.


```bash
#!/bin/bash

for file in "$@"; do
  if [[ "$file" =~ \.(c|js|py)$ ]]; then
    first_line=$(head -n 1 "$file")
    if [[ "$first_line" =~ ^# ]] || [[ "$first_line" =~ ^// ]]; then
      echo "$file has a comment in the first line."
    else
      echo "$file does not have a comment in the first line."
    fi
  fi
done

```
![img_11.png](img_11.png)
### Задача 7
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).
```bash
find "./" -type f -exec md5sum {} + | sort | uniq -w32 -dD
```
![img_12.png](img_12.png)
### Задача 8
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.
```bash
#!/bin/bash

find . -name "*.$1" -print0 | tar -czvf archive.tar.gz --null -T -
```
![img_13.png](img_13.png)
### Задача 9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
```bash
#!/bin/bash

sed 's/    /\t/g' "$1" > "$2"
```
### Задача 10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
```bash
find "$1" -type f -empty -name "*.txt"
```
![img_14.png](img_14.png)
