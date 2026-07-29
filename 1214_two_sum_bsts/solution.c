// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

bool twoSumBSTs(struct TreeNode* root1, struct TreeNode* root2, int target) {
    int values[1000];
    int count = 0;
    struct TreeNode* stack1[1000];
    int top1 = 0;
    if (root1) stack1[top1++] = root1;
    while (top1 > 0) {
        struct TreeNode* node = stack1[--top1];
        values[count++] = node->val;
        if (node->left) stack1[top1++] = node->left;
        if (node->right) stack1[top1++] = node->right;
    }
    struct TreeNode* stack2[1000];
    int top2 = 0;
    if (root2) stack2[top2++] = root2;
    while (top2 > 0) {
        struct TreeNode* node = stack2[--top2];
        int need = target - node->val;
        for (int i = 0; i < count; i++) {
            if (values[i] == need) return true;
        }
        if (node->left) stack2[top2++] = node->left;
        if (node->right) stack2[top2++] = node->right;
    }
    return false;
}
