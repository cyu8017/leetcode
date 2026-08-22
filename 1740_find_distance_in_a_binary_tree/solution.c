// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static struct TreeNode* lowestCommonAncestor(struct TreeNode* root, int p, int q) {
    if (root == NULL || root->val == p || root->val == q) {
        return root;
    }
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left != NULL && right != NULL) {
        return root;
    }
    return left != NULL ? left : right;
}

static int depthOf(struct TreeNode* root, int target) {
    if (root == NULL) {
        return -1;
    }
    if (root->val == target) {
        return 0;
    }
    int left = depthOf(root->left, target);
    if (left >= 0) {
        return left + 1;
    }
    int right = depthOf(root->right, target);
    if (right >= 0) {
        return right + 1;
    }
    return -1;
}

int findDistance(struct TreeNode* root, int p, int q) {
    struct TreeNode* ancestor = lowestCommonAncestor(root, p, q);
    return depthOf(ancestor, p) + depthOf(ancestor, q);
}
