#include <stdio.h>
#include <stdlib.h>

#define HASHSIZE 16

typedef struct Node *List;
struct Node {
  int value;
  struct Node *next;
};

typedef struct BST_Node *BSTree;
struct BST_Node {
  int value;
  struct BST_Node *right;
  struct BST_Node *left;
};


List crear_lista(List lista, char[2000]);
void mostrar_lista(List lista);
int esta_en_lista(int value, BSTree pasados[ HASHSIZE ]);
int esta_en_arbol(int value, BSTree *pasados);
List sacar_duplicados(List lista, BSTree *pasados);

int main() {
	List lista; 
	BSTree pasados[ HASHSIZE ];

	lista = NULL;
  int x;
  for(x=0; x<HASHSIZE; x++) {
    pasados[x] = NULL;
  }
	printf("Ingrese una lista de enteros separados por coma:");

	char str[2000] = "";
	scanf("%s", str);
	lista = crear_lista(lista, str);
	printf("La lista es: \n");
	mostrar_lista(lista);

	printf("\n\n");

	List rList = lista;

	printf("\n\nSacando Duplicados Queda: ");
	sacar_duplicados(lista, pasados);
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

int esta_en_lista(int value, BSTree pasados[ HASHSIZE ]) {
  return esta_en_arbol(value, &(pasados[ (value % HASHSIZE)  ]));
}

int esta_en_arbol(int value, BSTree *pasados) {	
  BSTree cursor = *pasados;

  //El nodo esta vacio
  if( cursor == NULL) {
    BSTree temp = (BSTree) malloc(sizeof(struct BST_Node));
    temp->value = value;
    temp->right = NULL;
    temp->left = NULL;
    *pasados = temp;
    return -1;
  }

  //El nodo tiene el mismo valor
  if( cursor->value == value ) return 1;

  if( cursor->value < value) {
      //Fijarse en el nodo derecho
      return esta_en_arbol(value, &(cursor->right));
   } else {
      //Fijarse en el nodo izquierdo
      return esta_en_arbol(value, &(cursor->left));
   }
}


List sacar_duplicados(List lista, BSTree *pasados) {
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
