// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* mergeNodes(struct ListNode* head) {
    struct ListNode dummy = {0, NULL};
    struct ListNode* cur = &dummy;
    int sum = 0;
    for (struct ListNode* p = head->next; p; p = p->next) {
        if (p->val == 0) {
            cur->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            cur->next->val = sum;
            cur->next->next = NULL;
            cur = cur->next;
            sum = 0;
        } else sum += p->val;
    }
    return dummy.next;
}
