// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minimumOperations(struct TreeNode* root) {
    if (!root) return 0;
    struct TreeNode** q = (struct TreeNode**)malloc(100000 * sizeof(struct TreeNode*));
    int head = 0, tail = 0;
    q[tail++] = root;
    int ans = 0;
    int* vals = (int*)malloc(100000 * sizeof(int));
    int* sorted = (int*)malloc(100000 * sizeof(int));
    while (head < tail) {
        int sz = tail - head;
        for (int i = 0; i < sz; i++) {
            struct TreeNode* node = q[head++];
            vals[i] = node->val;
            if (node->left) q[tail++] = node->left;
            if (node->right) q[tail++] = node->right;
        }
        memcpy(sorted, vals, (size_t)sz * sizeof(int));
        qsort(sorted, (size_t)sz, sizeof(int), cmp_int);
        /* map value -> index; values unique per constraints */
        for (int i = 0; i < sz; i++) {
            if (vals[i] != sorted[i]) {
                int j = i + 1;
                while (j < sz && vals[j] != sorted[i]) j++;
                int tmp = vals[i];
                vals[i] = vals[j];
                vals[j] = tmp;
                ans++;
            }
        }
    }
    free(q); free(vals); free(sorted);
    return ans;
}
