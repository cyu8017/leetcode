// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

long long* zigzagLevelSum(struct TreeNode* root, int* returnSize) {
    if (!root) { *returnSize = 0; return NULL; }
    struct TreeNode** q = malloc(1024 * sizeof(struct TreeNode*));
    int qcap = 1024, qn = 0;
    q[qn++] = root;
    bool left = true;
    long long* ans = malloc(1024 * sizeof(long long));
    int an = 0, acap = 1024;
    while (qn > 0) {
        struct TreeNode** nq = malloc((size_t)(qn * 2 + 8) * sizeof(struct TreeNode*));
        int nn = 0;
        for (int i = 0; i < qn; i++) {
            if (q[i]->left) nq[nn++] = q[i]->left;
            if (q[i]->right) nq[nn++] = q[i]->right;
        }
        int m = qn;
        long long s = 0;
        for (int i = 0; i < m; i++) {
            struct TreeNode* node = left ? q[i] : q[m - i - 1];
            struct TreeNode* child = left ? node->left : node->right;
            if (!child) break;
            s += node->val;
        }
        if (an == acap) { acap *= 2; ans = realloc(ans, (size_t)acap * sizeof(long long)); }
        ans[an++] = s;
        left = !left;
        free(q);
        q = nq;
        qn = nn;
    }
    free(q);
    *returnSize = an;
    return ans;
}
