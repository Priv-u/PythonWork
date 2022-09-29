# Загружаем кодек для нормального раскодирования русского текста в
# кодировке utf-8
import codecs

filePath = u'' + "E:\\Projects\\Pyton\\01\\hello.txt"

# при открытии файла также указываем его кодировку
helloFile = codecs.open(filePath, 'r', "utf-8")

helloContent = helloFile.read()
print(helloContent)
helloFile.close()

print('Файл прочитан и закрыт')
