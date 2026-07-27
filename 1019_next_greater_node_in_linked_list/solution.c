// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

int* nextLargerNodes(struct ListNode* head, int* returnSize) {
    int cap = 16, n = 0;
    int* vals = (int*)malloc((size_t)cap * sizeof(int));
    while (head) {
        if (n == cap) {
            cap *= 2;
            vals = (int*)realloc(vals, (size_t)cap * sizeof(int));
        }
        vals[n++] = head->val;
        head = head->next;
    }
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && vals[stack[top - 1]] < vals[i])
            ans[stack[--top]] = vals[i];
        stack[top++] = i;
    }
    free(vals);
    free(stack);
    *returnSize = n;
    return ans;
}
