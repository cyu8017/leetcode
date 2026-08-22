// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode* cur = head;
    while (cur && cur->next) {
        int g = gcd(cur->val, cur->next->val);
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = g;
        node->next = cur->next;
        cur->next = node;
        cur = node->next;
    }
    return head;
}
