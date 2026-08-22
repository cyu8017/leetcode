// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int cmpLLDesc(const void* a, const void* b) {
    long long x = *(const long long*)a, y = *(const long long*)b;
    if (x > y) return -1;
    if (x < y) return 1;
    return 0;
}

long long kthLargestLevelSum(struct TreeNode* root, int k) {
    if (!root) return -1;
    struct TreeNode** q = (struct TreeNode**)malloc(100000 * sizeof(struct TreeNode*));
    long long* sums = (long long*)malloc(100000 * sizeof(long long));
    int sc = 0;
    int head = 0, tail = 0;
    q[tail++] = root;
    while (head < tail) {
        int sz = tail - head;
        long long s = 0;
        for (int i = 0; i < sz; i++) {
            struct TreeNode* node = q[head++];
            s += node->val;
            if (node->left) q[tail++] = node->left;
            if (node->right) q[tail++] = node->right;
        }
        sums[sc++] = s;
    }
    qsort(sums, (size_t)sc, sizeof(long long), cmpLLDesc);
    long long ans = k > sc ? -1 : sums[k - 1];
    free(q); free(sums);
    return ans;
}
