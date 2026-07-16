// LeetCode 0138 - Copy List with Random Pointer
#include <stdlib.h>
struct Node { int val; struct Node *next, *random; };
struct Node* copyRandomList(struct Node* head) {
    if (!head) return NULL;
    for (struct Node *node = head; node; node = node->next) {
        struct Node *copy = malloc(sizeof(struct Node));
        copy->val = node->val; copy->next = node->next; copy->random = NULL;
        node->next = copy;
    }
    for (struct Node *node = head; node; node = node->next->next)
        if (node->random) node->next->random = node->random->next;
    struct Node dummy = {0, NULL, NULL}, *tail = &dummy;
    for (struct Node *node = head; node;) {
        struct Node *copy = node->next;
        node->next = copy->next; node = node->next;
        tail->next = copy; tail = copy;
    }
    return dummy.next;
}