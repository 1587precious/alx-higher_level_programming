#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>

/**
 * struct Node - singly linked list
 * @value: integer
 * @nextNode: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct Node
{
	int value;
	struct Node *nextNode;
} Node;

size_t print_list(const Node *head);
Node *add_node_end(Node **head, const int value);
void free_list(Node *head);

int is_palindrome(Node **head);
int palindrome_check(Node **left, Node *right);

#endif /* LISTS_H */
