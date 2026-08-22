// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

static struct ListNode* rev(struct ListNode* node) {
    struct ListNode* prev = NULL;
    while (node) {
        struct ListNode* nxt = node->next;
        node->next = prev;
        prev = node;
        node = nxt;
    }
    return prev;
}

struct ListNode* doubleIt(struct ListNode* head) {
    head = rev(head);
    int carry = 0;
    struct ListNode* cur = head;
    struct ListNode* prev = NULL;
    while (cur) {
        int val = cur->val * 2 + carry;
        cur->val = val % 10;
        carry = val / 10;
        prev = cur;
        cur = cur->next;
    }
    if (carry > 0) {
        prev->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        prev->next->val = carry;
        prev->next->next = NULL;
    }
    return rev(head);
}
