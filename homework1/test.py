import unittest
from io import StringIO
from unittest.mock import patch
from main import *


# Тест-класс
class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=['exit'])  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_none(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '[bogdan] : archive :')

    @patch('builtins.input', side_effect='''ls\nexit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_1(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(),
'''[bogdan] : archive :         a  q  b  
         xrwxrwxrx
data     111110000
keys     111110000
rec.txt  111110000
system   111110000
user     111110000
[bogdan] : archive :''')

    @patch('builtins.input', side_effect='''fhfhf\n exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_2(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '''[bogdan] : archive :The name 'fhfhf' is not recognized as a command name\n[bogdan] : archive :''')

    @patch('builtins.input', side_effect='''cd /data\nexit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_3(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '[bogdan] : archive :[bogdan] : archive/data :')

    @patch('builtins.input', side_effect='''cd /dat
     exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_4(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '''[bogdan] : archive :Path '/dat' does not exist.
[bogdan] : archive :''')

    @patch('builtins.input', side_effect='''cd archive/user
    ls
    exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_5(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '''[bogdan] : archive :[bogdan] : archive/user :             a  q  b  
             xrwxrwxrx
apps         111110000
images       111110000
movies       111110000
music        111110000
my_text.txt  111110000
[bogdan] : archive/user :''')

    @patch('builtins.input', side_effect='''cd /data
    ls
    exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_6(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '''[bogdan] : archive :[bogdan] : archive/data :0 files
[bogdan] : archive/data :''')

    @patch('builtins.input', side_effect='''chmod ab+xr /data
     ls
     exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_7(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '''[bogdan] : archive :[b] : archive :         a  q  b  
         xrwxrwxrx
data     111110110
keys     111110000
rec.txt  111110000
system   111110000
user     111110000
[b] : archive :''')

    @patch('builtins.input', side_effect='''wc\n0\n0\nstop\nexit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_8(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '[bogdan] : archive :2 3 4\n[bogdan] : archive :')

    @patch('builtins.input', side_effect='''chmod\n exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_9(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '[bogdan] : archive :You need to specify a permission\n'
                                                 '[bogdan] : archive :')

    @patch('builtins.input', side_effect='''exit'''.split('\n'))  # Подменяем ввод на 'Alice'
    @patch('sys.stdout', new_callable=StringIO)  # Захватываем вывод
    def test_10(self, mock_output, mock_input):
        main_c()  # Вызываем main
        self.assertEqual(mock_output.getvalue(), '[bogdan] : archive :')


if __name__ == '__main__':
    unittest.main()
