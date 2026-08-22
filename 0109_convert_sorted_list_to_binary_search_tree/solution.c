// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static struct TreeNode* build(int* values, int left, int right) {
    if (left > right) {
        return NULL;
    }
    int mid = (left + right + 1) / 2;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = values[mid];
    root->left = build(values, left, mid - 1);
    root->right = build(values, mid + 1, right);
    return root;
}

struct TreeNode* sortedListToBST(struct ListNode* head) {
    int capacity = 16;
    int size = 0;
    int* values = (int*)malloc((size_t)capacity * sizeof(int));
    while (head) {
        if (size >= capacity) {
            capacity *= 2;
            values = (int*)realloc(values, (size_t)capacity * sizeof(int));
        }
        values[size++] = head->val;
        head = head->next;
    }
    struct TreeNode* root = build(values, 0, size - 1);
    free(values);
    return root;
}
