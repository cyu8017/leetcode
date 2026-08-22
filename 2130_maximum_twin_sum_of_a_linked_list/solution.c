// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

int pairSum(struct ListNode* head) {
    struct ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode* prev = NULL;
    while (slow) {
        struct ListNode* nxt = slow->next;
        slow->next = prev;
        prev = slow;
        slow = nxt;
    }
    int ans = 0;
    struct ListNode *a = head, *b = prev;
    while (b) {
        if (a->val + b->val > ans) ans = a->val + b->val;
        a = a->next;
        b = b->next;
    }
    return ans;
}
