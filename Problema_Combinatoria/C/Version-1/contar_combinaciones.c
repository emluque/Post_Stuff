#include <stdio.h>
#include <stdlib.h>
#include "lista.c"
#include "combinaciones.c"
#include "factorizar.c"

#define MAX_ALPHABET_SIZE 7
#define MAX_STRING_SIZE 7


int contar_elementos_distintos(List lista, int alphabet_size);
void mostrar_todo( int arr[ MAX_ALPHABET_SIZE ][ MAX_STRING_SIZE ][ MAX_ALPHABET_SIZE ] );
void mostrar_todo_factorizado( int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE] );

int main() {
	int k,n,z;
 	//k: Tamaño de alfabeto
	//n: Tamaño de cadena
	//z: cantidad de simbolos en la combinacion 	

	int arr[MAX_ALPHABET_SIZE][MAX_STRING_SIZE][MAX_ALPHABET_SIZE];
	//Inicializar array
	for(k=0; k<MAX_ALPHABET_SIZE; k++) {
		for(n=0; n<MAX_STRING_SIZE; n++) {
			for(z=0; z<MAX_ALPHABET_SIZE; z++) {
				arr[ k ][ n ][ z ] = 0;
			}
		}
	}

	Result_list results;
	int contar = 0;

	for(k=0; k<MAX_ALPHABET_SIZE; k++) {
//		printf("K:%d\n", k);
		for(n=0; n<MAX_STRING_SIZE; n++) {
//			printf("n:%d\n", (n+1)); 
			results = generar_combinaciones(n, k);
//			mostrar_combinaciones(results);
			while( results != NULL) {
				contar = contar_elementos_distintos(results->list, k); //No se si esto esta bien 					
				arr[ k ][ n ][ contar ]++;
				results = results->next;
			}
			//Liberar results!!!!
			liberar_results(results);
		}
	}
	
	mostrar_todo(arr);
	mostrar_todo_factorizado(arr);

	return 0;
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

