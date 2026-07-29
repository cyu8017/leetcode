// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

#include <functional>
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* constructFromPrePost(std::vector<int>& preorder,
                                   std::vector<int>& postorder) {
        std::unordered_map<int, int> postIndex;
        for (int i = 0; i < static_cast<int>(postorder.size()); ++i) {
            postIndex[postorder[i]] = i;
        }
        std::function<TreeNode*(int, int, int, int)> build =
            [&](int preLo, int preHi, int postLo, int postHi) -> TreeNode* {
            if (preLo > preHi) {
                return nullptr;
            }
            TreeNode* root = new TreeNode(preorder[preLo]);
            if (preLo == preHi) {
                return root;
            }
            int leftVal = preorder[preLo + 1];
            int leftPost = postIndex[leftVal];
            int leftSize = leftPost - postLo + 1;
            root->left = build(preLo + 1, preLo + leftSize, postLo, leftPost);
            root->right =
                build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1);
            return root;
        };
        int n = static_cast<int>(preorder.size());
        return build(0, n - 1, 0, n - 1);
    }
};
