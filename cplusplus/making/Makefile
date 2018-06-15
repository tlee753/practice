CC = g++
CFLAGS = -c -Wall -std=c++14 

all: hello

hello: Main.o Car.o
	$(CC) Main.o Car.o -o hello

Main.o: Main.cpp
	$(CC) $(CFLAGS) Main.cpp

Car.o: Car.cpp
	$(CC) $(CFLAGS) Car.cpp
 
clean: 
	rm -rf *o hello
