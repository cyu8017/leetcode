// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

#include <stdlib.h>

struct Node {
    int val;
    struct Node* prev;
    struct Node* next;
};

int* toArray(struct Node* head, int* returnSize) {
    int cap = 16, n = 0;
    int* ans = (int*)malloc((size_t)cap * sizeof(int));
    while (head) {
        if (n == cap) { cap *= 2; ans = (int*)realloc(ans, (size_t)cap * sizeof(int)); }
        ans[n++] = head->val;
        head = head->next;
    }
    *returnSize = n;
    return ans;
}
