// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

static int depth(struct TreeNode* node, int* best) {
    if (!node) {
        return 0;
    }
    const int left = depth(node->left, best);
    const int right = depth(node->right, best);
    if (left + right > *best) {
        *best = left + right;
    }
    return 1 + maxInt(left, right);
}

int diameterOfBinaryTree(struct TreeNode* root) {
    int best = 0;
    depth(root, &best);
    return best;
}
