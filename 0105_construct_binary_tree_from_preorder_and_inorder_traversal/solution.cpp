// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#include <unordered_map>
#include <vector>

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
    TreeNode* buildTree(std::vector<int>& preorder, std::vector<int>& inorder) {
        std::unordered_map<int, int> index;
        for (int i = 0; i < (int)inorder.size(); i++) {
            index[inorder[i]] = i;
        }
        int preIndex = 0;
        return build(preorder, index, preIndex, 0, (int)inorder.size() - 1);
    }

private:
    TreeNode* build(std::vector<int>& preorder, std::unordered_map<int, int>& index,
                    int& preIndex, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        int rootVal = preorder[preIndex++];
        int mid = index[rootVal];
        TreeNode* root = new TreeNode(rootVal);
        root->left = build(preorder, index, preIndex, left, mid - 1);
        root->right = build(preorder, index, preIndex, mid + 1, right);
        return root;
    }
};