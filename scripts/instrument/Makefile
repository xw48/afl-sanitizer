all: asandump.c
	gcc -lasan -c asandump.c
	ar cr libasandump.a asandump.o

clean:
	rm -rf asandump.o libasandump.a
