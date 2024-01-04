#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @head: pointer to linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
    listint_t *turtle = head, *hare = head;

    while (hare != NULL && hare->next != NULL)
    {
        turtle = turtle->next;
        hare = hare->next->next;

        if (turtle == hare)
            return 1;
    }
    return 0;
}
