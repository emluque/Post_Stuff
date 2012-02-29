#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#include "combinaciones.h"

struct Result {
	List list;
	struct Result *next;
};

void liberar_results(Result_list result_list) {
	Result_list result_list_temp_cursor;

	while(result_list != NULL) {
		liberar_lista(result_list->list);
		result_list_temp_cursor = result_list->next;
		free(result_list);
		result_list = result_list_temp_cursor;
	}		

}


Result_list generar_combinaciones(int depth, int size) {
	Result_list results = NULL;
	Result_list cursor;

	int x;	

	if(depth == 0) {
		for(x=0; x<size; x++) {
			List temp;
			temp = (List) malloc(sizeof(struct Node));
			temp->value = x;
			temp->next = NULL;

			Result_list temp_result;
			temp_result = (Result_list) malloc(sizeof(struct Result));
			temp_result->list = temp;
			temp_result->next = NULL;

			if(results == NULL) {
				results = temp_result;
				cursor = temp_result;
			} else {
				cursor->next = temp_result;
				cursor = cursor->next;
			}
		}
		return results;
	} else {
		Result_list previous_results;
		Result_list previous_temp_cursor;

		previous_results = generar_combinaciones(depth-1, size);
		
		while(previous_results != NULL) {
			for(x=0; x<size; x++) {
				List temp;
				temp = (List) malloc(sizeof(struct Node));
				temp->value = x;
				temp->next = previous_results->list;

				Result_list temp_result;
				temp_result = (Result_list) malloc(sizeof(struct Result));
				temp_result->list = temp;
				temp_result->next = NULL;

				if(results == NULL) {
					results = temp_result;
					cursor = temp_result;
				} else {
					cursor->next = temp_result;
					cursor = cursor->next;
				}
			}
			previous_temp_cursor = previous_results->next;
			free(previous_results);
			previous_results = previous_temp_cursor;			
		}
		return results;
	}
} 

void mostrar_combinaciones(Result_list results) {
	while(results != NULL) {
		mostrar_lista(results->list);
		results = results->next;
		printf("\n");
	}
}
