all: Web

Web: Web.c
	gcc -W -Wall -lpthread -o service Web.c

clean:
	rm service
