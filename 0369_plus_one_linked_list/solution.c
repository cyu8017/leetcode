// LeetCode 0369 - Plus One Linked List
// https://leetcode.com/problems/plus-one-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* plusOne(struct ListNode* head) {
    struct ListNode sentinel = {0, head};
    struct ListNode* notNine = &sentinel;
    struct ListNode* node = head;

    while (node != NULL) {
        if (node->val != 9) {
            notNine = node;
        }
        node = node->next;
    }

    notNine->val += 1;
    node = notNine->next;
    while (node != NULL) {
        node->val = 0;
        node = node->next;
    }

    if (sentinel.val == 1) {
        struct ListNode* newHead = (struct ListNode*)malloc(sizeof(struct ListNode));
        newHead->val = 1;
        newHead->next = sentinel.next;
        return newHead;
    }

    return sentinel.next;
}
