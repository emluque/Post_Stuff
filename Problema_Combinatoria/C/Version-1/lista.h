#ifndef _list_h
#define _list_h

typedef struct Node *List;

void mostrar_lista(List lista);
List agregar_valor_a_lista(int i, List factores);
void liberar_lista(List lista);

#endif
