#ifndef _combinaciones_h
#define _combinaciones_h

typedef struct Result *Result_list;

Result_list generar_combinaciones(int depth, int size);
void mostrar_combinaciones(Result_list results);
void liberar_results(Result_list results);

#endif
