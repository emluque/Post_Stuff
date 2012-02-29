#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

struct Node {
  int value;
  struct Node *next;
};

void mostrar_lista(List lista) {
	//Este primer paso es para el pretty print de la lista
	if(lista != NULL) {
		printf("%d", lista->value);
		lista = lista->next;
	}
	while(lista != NULL) {
		printf("-%d", lista->value);
		lista = lista->next;
	}
}

List agregar_valor_a_lista(int i, List factores) {
	List temp;
	temp = (List) malloc(sizeof(struct Node));
	temp->value = i;
	temp->next = NULL;

	if(factores == NULL) {
		return temp;
		
	} else {
		List cursor = factores;
		while(cursor->next != NULL) cursor = cursor->next;
		cursor->next = temp;
		return factores;
	}

}

void liberar_lista(List lista) {
	List list_swap;
	while(lista != NULL) {
		list_swap = lista->next;
		free(lista);
		lista = list_swap;
	}
}
