// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

struct TreeNode* getTargetCopy(struct TreeNode* original, struct TreeNode* cloned, struct TreeNode* target) {
    if (!original) return NULL;
    if (original == target) return cloned;
    struct TreeNode* L = getTargetCopy(original->left, cloned->left, target);
    if (L) return L;
    return getTargetCopy(original->right, cloned->right, target);
}
