// LeetCode 1305 - All Elements in Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static void inorder(struct TreeNode* root, int** buf, int* size, int* cap) {
    if (!root) return;
    inorder(root->left, buf, size, cap);
    if (*size == *cap) {
        *cap *= 2;
        *buf = (int*)realloc(*buf, (*cap) * sizeof(int));
    }
    (*buf)[(*size)++] = root->val;
    inorder(root->right, buf, size, cap);
}

int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize) {
    int cap1 = 16, cap2 = 16, n1 = 0, n2 = 0;
    int* a = (int*)malloc(cap1 * sizeof(int));
    int* b = (int*)malloc(cap2 * sizeof(int));
    inorder(root1, &a, &n1, &cap1);
    inorder(root2, &b, &n2, &cap2);
    int* ans = (int*)malloc((n1 + n2) * sizeof(int));
    int i = 0, j = 0, k = 0;
    while (i < n1 || j < n2) {
        if (j == n2 || (i < n1 && a[i] <= b[j])) ans[k++] = a[i++];
        else ans[k++] = b[j++];
    }
    free(a); free(b);
    *returnSize = k;
    return ans;
}
