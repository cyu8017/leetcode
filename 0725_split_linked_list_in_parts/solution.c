// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize) {
    int length = 0;
    for (struct ListNode* node = head; node; node = node->next) {
        length++;
    }
    int partSize = length / k;
    int extra = length % k;
    struct ListNode** result = (struct ListNode**)malloc((size_t)k * sizeof(struct ListNode*));
    struct ListNode* current = head;
    for (int i = 0; i < k; i++) {
        result[i] = current;
        int size = partSize + (i < extra ? 1 : 0);
        for (int j = 0; j < size - 1; j++) {
            if (current) {
                current = current->next;
            }
        }
        if (current) {
            struct ListNode* nxt = current->next;
            current->next = NULL;
            current = nxt;
        }
    }
    *returnSize = k;
    return result;
}
