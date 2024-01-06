#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome
 *
 * @head: Head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (!*head || !(*head))
	{
		/* An empty list or a single-node list is a palindrome */
		return (1);
	}

	if (p_check(head, *head))
	{
		return (1);
	}

	return (0);
}

/**
 * p_check - Helper function to check for palindrome recursively
 *
 * @left: Pointer to the left side of the list
 * @right: Pointer to the right side of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */

int p_check(listint_t **left, listint_t *right)
{
	int is_p = 0;

	if (right)
	{
		is_p = p_check(left, right->next);
	}
	else
	{
		/* Reached the end of the list, indicating a palindrome */
		return (1);
	}

	if (is_p == 1)
	{
		if ((*left)->n == right->n)
		{
			/* Move the left pointer to the next node */
			(*left) = (*left)->next;
			return (1);
		}
	}

	/* Not a palindrome */
	return (0);
}
