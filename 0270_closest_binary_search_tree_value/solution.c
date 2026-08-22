// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

#include <math.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int closestValue(struct TreeNode* root, double target) {
    int closest = root->val;
    struct TreeNode* current = root;
    while (current) {
        if (fabs((double)closest - target) > fabs((double)current->val - target)) {
            closest = current->val;
        }
        if ((double)current->val == target) {
            return current->val;
        }
        current = target < (double)current->val ? current->left : current->right;
    }
    return closest;
}
