// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

static struct ListNode* rev2487(struct ListNode* node) {
    struct ListNode* prev = NULL;
    while (node) {
        struct ListNode* nxt = node->next;
        node->next = prev;
        prev = node;
        node = nxt;
    }
    return prev;
}

struct ListNode* removeNodes(struct ListNode* head) {
    head = rev2487(head);
    int mx = 0;
    struct ListNode dummy = {0, head};
    struct ListNode* prev = &dummy;
    while (prev->next) {
        if (prev->next->val >= mx) {
            mx = prev->next->val;
            prev = prev->next;
        } else {
            prev->next = prev->next->next;
        }
    }
    return rev2487(dummy.next);
}
