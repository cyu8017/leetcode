// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct ListNode** splitCircularLinkedList(struct ListNode* list, int* returnSize) {
    struct ListNode** ans = (struct ListNode**)malloc(2 * sizeof(struct ListNode*));
    *returnSize = 2;
    if (!list) { ans[0] = ans[1] = NULL; return ans; }
    struct ListNode *slow = list, *fast = list;
    while (fast->next != list && fast->next->next != list) {
        slow = slow->next;
        fast = fast->next->next;
    }
    if (fast->next->next == list) fast = fast->next;
    struct ListNode* head2 = slow->next;
    slow->next = list;
    fast->next = head2;
    ans[0] = list;
    ans[1] = head2;
    return ans;
}
