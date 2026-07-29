// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int cameras;

static int dfs(struct TreeNode* node) {
    if (!node) return 1;
    int left = dfs(node->left), right = dfs(node->right);
    if (left == 0 || right == 0) { cameras++; return 2; }
    if (left == 2 || right == 2) return 1;
    return 0;
}

int minCameraCover(struct TreeNode* root) {
    cameras = 0;
    int st = dfs(root);
    return cameras + (st == 0 ? 1 : 0);
}
