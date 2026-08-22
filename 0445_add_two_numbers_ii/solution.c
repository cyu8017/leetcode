// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int stack1[10000];
    int stack2[10000];
    int top1 = 0;
    int top2 = 0;

    while (l1) {
        stack1[top1++] = l1->val;
        l1 = l1->next;
    }
    while (l2) {
        stack2[top2++] = l2->val;
        l2 = l2->next;
    }

    int carry = 0;
    struct ListNode* head = NULL;
    while (top1 > 0 || top2 > 0 || carry) {
        int total = carry;
        if (top1 > 0) {
            total += stack1[--top1];
        }
        if (top2 > 0) {
            total += stack2[--top2];
        }
        carry = total / 10;
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = total % 10;
        node->next = head;
        head = node;
    }
    return head;
}
