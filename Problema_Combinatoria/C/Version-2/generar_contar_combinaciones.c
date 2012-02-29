#include <stdio.h>
#include <stdlib.h>
#include "lista.c"
#include "factorizar.c"

#define MAX_ALPHABET_SIZE 5
#define MAX_STRING_SIZE 5

void generar_contar_combinaciones(int depth, int size, List lista, int arr[MAX_ALPHABET_SIZE]);
int contar_elementos_distintos(List lista, int alphabet_size);
void mostrar_todo( int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE] );
void mostrar_todo_factorizado( int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE] );

int main() {
	List lista = NULL;
	int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE];
	int x,y,z;
	//Inicializar arr
	for(x=0; x<MAX_ALPHABET_SIZE; x++) {
		for(y=0; y<MAX_STRING_SIZE; y++) {
			for(z=0; z<MAX_ALPHABET_SIZE;z++) {
				arr[x][y][z] = 0;
			}
		}
	}

	for(x=0; x<MAX_ALPHABET_SIZE; x++) {
		for(y=0; y<MAX_STRING_SIZE; y++) {
			generar_contar_combinaciones(y, x, lista, arr[x][y]);
		}
	}

	mostrar_todo(arr);
	mostrar_todo_factorizado(arr);

	printf("</body></html>");
}

int contar_elementos_distintos(List lista, int alphabet_size) {
	int symbols[ alphabet_size ];
	int x;
	int count = 0;
	
	//Inicializar array
	for(x=0; x<alphabet_size; x++) {
		symbols[ x ] = 0;
	}
		

	while(lista != NULL) {
		symbols[ lista->value ] ++;
		lista = lista->next;		
	}

	for(x=0; x<alphabet_size; x++) {
		if( symbols[ x ] > 0) count++;
	}

	return count;
} 

void generar_contar_combinaciones(int depth, int size, List lista, int arr[MAX_ALPHABET_SIZE]) {
	int x, c;	
	List cursor_ultimo = lista;

	if(cursor_ultimo != NULL) {
		while(cursor_ultimo->next != NULL) cursor_ultimo = cursor_ultimo->next;
	}

	if(depth == 0) {
		for(x=0; x<size; x++) {
			List temp;
			temp = (List) malloc(sizeof(struct Node));
			temp->value = x;
			temp->next = NULL;

			if(cursor_ultimo == NULL) {
				c = contar_elementos_distintos(temp, size);
				arr[ c ]++;
				free(temp);
			} else {
				cursor_ultimo->next = temp;
				c = contar_elementos_distintos(lista, size);
				arr[ c ]++;
				free(temp);
				cursor_ultimo->next = NULL;
			}
		}
	} else {
		for(x=0; x<size; x++) {
			List temp;
			temp = (List) malloc(sizeof(struct Node));
			temp->value = x;
			temp->next = NULL;

			if(cursor_ultimo == NULL) {
				generar_contar_combinaciones(depth-1, size, temp, arr);
				free(temp);
			} else {
				cursor_ultimo->next = temp;
				generar_contar_combinaciones(depth-1, size, lista, arr);
				free(temp);
				cursor_ultimo->next = NULL;
			}
		}
	}
}

void mostrar_todo( int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE] ) {
	int k, n, z;

	printf("<html><head><title>Problema de Combinatoria</title>");
	printf("<style type='text/css'> td, table {border: 1px solid black} td { width: 20px;}</style>");
	printf("</head><body>");
	printf("<h1>Problema de combinatoria</h1>");
	printf("<p>Sea A un alfabeto de k simbolos.</p>");
	printf("<p>Calcular cuantas cadenas de tamaño n pueden ser construidas con exactamente z simbolos distintos de k.</p>");
	printf("<h2>Resultados</h2>");
	for(k=0; k<MAX_ALPHABET_SIZE; k++) {
		printf("<h3>Alfabeto de tamaño: %d</h3>", k);
		printf("<table>");
		for(n=0; n<MAX_STRING_SIZE; n++) {
			printf("<tr>");
			printf("<td style='width: 200px; font-weight: bold;'>Cadena de tamaño: %d</td>", (n+1));
			for(z=0; z<MAX_ALPHABET_SIZE; z++) {
				printf("<td>%d</td>", arr[ k ][ n ][ z ]);
			}
			printf("</tr>");	
		}
		printf("</table>");
	}

}

void mostrar_todo_factorizado( int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE] ) {
	int k, n, z;
	List factores;

	printf("<h2>Resultados factorizados</h2>");
	for(k=0; k<MAX_ALPHABET_SIZE; k++) {
		printf("<h3>Alfabeto de tamaño: %d</h3>", k);
		printf("<table>");
		for(n=0; n<MAX_STRING_SIZE; n++) {
			printf("<tr>");
			printf("<td style='width: 200px; font-weight: bold;'>Cadena de tamaño: %d</td>", (n+1));
			for(z=0; z<MAX_ALPHABET_SIZE; z++) {
				printf("<td>");
				factores = factorizar( arr[ k ][ n ][ z ]);
				mostrar_lista(factores);
				printf("</td>");
				liberar_lista(factores);
			}
			printf("</tr>");	
		}
		printf("</table>");
	}

}
