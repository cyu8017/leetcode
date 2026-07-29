// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

#include <stddef.h>

struct Node {
    int val;
    struct Node* prev;
    struct Node* next;
    struct Node* child;
};

struct Node* flatten(struct Node* head) {
    struct Node* current = head;
    while (current) {
        if (current->child) {
            struct Node* nextNode = current->next;
            struct Node* childHead = flatten(current->child);
            current->next = childHead;
            childHead->prev = current;
            struct Node* tail = childHead;
            while (tail->next) {
                tail = tail->next;
            }
            tail->next = nextNode;
            if (nextNode) {
                nextNode->prev = tail;
            }
            current->child = NULL;
        }
        current = current->next;
    }
    return head;
}
