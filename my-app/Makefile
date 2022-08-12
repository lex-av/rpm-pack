all: myapp
CC = gcc
myapp: main.c
	$(CC) -o myapp  main.c
dist: myapp_1.0.tar.gz
myapp_1.0.tar.gz: myapp
	-rm -rf -f myapp-1.0
	mkdir myapp-1.0
	cp *.c Makefile myapp-1.0
	tar zcvf $@ myapp-1.0
	-rm -rf -f myapp-1.0
