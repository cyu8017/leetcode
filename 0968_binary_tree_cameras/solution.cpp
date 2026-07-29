// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int minCameraCover(TreeNode* root) {
        int cameras = 0;
        auto dfs = [&](auto&& self, TreeNode* node) -> int {
            if (!node) return 1;
            int left = self(self, node->left);
            int right = self(self, node->right);
            if (left == 0 || right == 0) {
                cameras++;
                return 2;
            }
            if (left == 2 || right == 2) return 1;
            return 0;
        };
        int rootState = dfs(dfs, root);
        return cameras + (rootState == 0 ? 1 : 0);
    }
};
