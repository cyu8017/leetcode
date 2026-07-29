// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int widthOfBinaryTree(struct TreeNode* root) {
    if (!root) return 0;
    struct TreeNode** nodes = (struct TreeNode**)malloc(3000 * sizeof(struct TreeNode*));
    unsigned long long* idxs = (unsigned long long*)malloc(3000 * sizeof(unsigned long long));
    int head = 0, tail = 0;
    nodes[tail] = root; idxs[tail] = 0; tail++;
    int best = 0;
    while (head < tail) {
        int level = tail - head;
        unsigned long long left = idxs[head];
        for (int i = 0; i < level; i++) {
            struct TreeNode* node = nodes[head];
            unsigned long long idx = idxs[head];
            head++;
            int width = (int)(idx - left + 1);
            if (width > best) best = width;
            if (node->left) { nodes[tail] = node->left; idxs[tail] = idx * 2; tail++; }
            if (node->right) { nodes[tail] = node->right; idxs[tail] = idx * 2 + 1; tail++; }
        }
    }
    free(nodes); free(idxs);
    return best;
}
