all: Web

Web: Web.c
	gcc  Web.c -lpthread -o service

clean:
	rm service
