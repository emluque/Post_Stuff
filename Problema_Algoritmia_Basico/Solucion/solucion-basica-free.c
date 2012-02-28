#include <stdio.h>
#include <stdlib.h>


typedef struct Node *List;
struct Node {
  int value;
  struct Node *next;
};



List crear_lista(List lista, char[2000]);
void mostrar_lista(List lista);
int esta_en_lista(int value, List *pasados);
List sacar_duplicados(List lista, List *pasados);

int main() {
	List lista, pasados; 

	lista = NULL;
	pasados = NULL;

	printf("Ingrese una lista de enteros separados por coma:");

	char str[2000] = "";
	scanf("%s", str);
	lista = crear_lista(lista, str);
	printf("La lista es: \n");
	mostrar_lista(lista);

	printf("\n\n");

	List rList = lista;

	printf("\n\nSacando Duplicados Queda: ");
	sacar_duplicados(lista, &pasados);
	mostrar_lista(lista);
	
	printf("\n\n");


}

List crear_lista(List lista, char str[2000]) {
	int i=0;
	List rList = lista;

	//Es forgiving, solo lee los digitos y descarta lo demas.
	while( str[i] != '\0' ) {
		while( str[i] != '\0' && (str[i] < '0' || str[i] > '9') ) i++;
		if(str[i] == '\0') break;

		int pre = 0;
	    
		//Calcular el int
		while( str[i] != ',' && str[i] != '\0' ) {
			if(!(str[i] < '0' || str[i] > '9')) { 
				pre = pre * 10;
				pre = pre + (str[i] - '0');
			} 
			i++; 
		}
	    
		//Crear el nodo nuevo    
		List temp;
		temp = (List) malloc(sizeof(struct Node));
		temp->value = pre;
		temp->next = NULL;

		//Primera iteracion
		if(lista==NULL) {
			//Agregar nodo a lista
			lista = temp;
			//Lista de retorno
			rList = lista;
		} else {
			//Agregar nodo, mover cursor.
			lista->next = temp;
			lista = lista->next;
		} 
		i++;
	}
	return rList;
}

//Version basica a ser mejorada
//Se pasa un puntero al puntero de lista para hacer los side effects
int esta_en_lista(int value, List *pasados) {

	List rList, prev;

	rList = *pasados;
	prev = NULL;

	if(rList == NULL) {
		//Agregarlo antes
		List temp;
		temp = (List) malloc(sizeof(struct Node));
		temp->value = value;
		temp->next = *pasados;
		*pasados = temp;
		return -1;
	}

	while(rList != NULL) {
		if(rList->value == value) return 1;
		if(rList->value > value) {
			List temp;
			temp = (List) malloc(sizeof(struct Node));
			temp->value = value;
			temp->next = rList;
			if(prev==NULL) {
				*pasados = temp;
			} else {
				prev->next = temp;
			}
			return -1;
		}
		prev = rList;
		rList = rList->next;
	}
	//Agregarlo al final
	List temp;
	temp = (List) malloc(sizeof(struct Node));
	temp->value = value;
	temp->next = NULL;
	prev->next = temp;
	return -1;
}



//ESTA ES LA FUNCION QUE IMPORTA EN UN PRIMER PASO
//EN UN SEGUNDO PASO LO QUE IMPORTA ES MEJORAR LA FUNCION ANTERIOR
List sacar_duplicados(List lista, List *pasados) {
	//Caso Base
	if( lista == NULL) {
		return lista;
	} else {
	//PASO INDUCTIVO
		if( esta_en_lista( lista->value, pasados) > 0 ) {
			List next = lista->next;
			free( lista );
			return sacar_duplicados( next, pasados);
		} else {
			lista->next = sacar_duplicados( lista->next, pasados );
			return lista;
		}
	}
}


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
