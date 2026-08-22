// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

#include <stdlib.h>

struct Node {
    int val;
    struct Node* next;
};

struct Node* insert(struct Node* head, int insertVal) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->val = insertVal;
    node->next = NULL;
    if (!head) {
        node->next = node;
        return node;
    }

    struct Node* cur = head;
    while (cur->next && cur->next != head) {
        cur = cur->next;
    }
    cur->next = head;

    struct Node* prev = head;
    struct Node* curr = head->next;
    while (1) {
        if (prev->val <= insertVal && insertVal <= curr->val) {
            break;
        }
        if (prev->val > curr->val && (insertVal >= prev->val || insertVal <= curr->val)) {
            break;
        }
        prev = curr;
        curr = curr->next;
        if (prev == head) {
            break;
        }
    }
    prev->next = node;
    node->next = curr;
    return head;
}
