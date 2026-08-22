// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

#include <stdlib.h>

struct Node {
    int val;
    struct Node* prev;
    struct Node* next;
};

int* toArray(struct Node* node, int* returnSize) {
    while (node && node->prev) node = node->prev;
    int cap = 16, n = 0;
    int* ans = (int*)malloc((size_t)cap * sizeof(int));
    while (node) {
        if (n == cap) { cap *= 2; ans = (int*)realloc(ans, (size_t)cap * sizeof(int)); }
        ans[n++] = node->val;
        node = node->next;
    }
    *returnSize = n;
    return ans;
}
