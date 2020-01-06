all: Web

Web: Web.c
	gcc -W -Wall Web.c -lpthread -o service

clean:
	rm service
