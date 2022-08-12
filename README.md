### RPM-пакет

Репозиторий содержит собранный пакет myapp.rpm, содержащий простую программу на С, выводящую в STDOUT "Test task in RAIDIX!", для установки пакетным
мэнеджером rpm и папку myapp с исходным кодом, make-файлом и spec-файлом.

Для сборки пакета используются команды:

make dist в директории my-app для сборки .tag.gz архива

cp myapp_1.0.tag.gz /home/(username)/rpmbuild/SOURCES/ для копирования полученого архива в директорию rpmbuild 

rpmbuild -ba myapp.spec в директории my-app для сборки rpm-пакета
