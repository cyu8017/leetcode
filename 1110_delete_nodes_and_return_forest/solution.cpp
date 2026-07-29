// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

#include <unordered_set>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::vector<TreeNode*> delNodes(TreeNode* root, std::vector<int>& to_delete) {
        std::unordered_set<int> deleteSet(to_delete.begin(), to_delete.end());
        std::vector<TreeNode*> forest;
        dfs(root, true, deleteSet, forest);
        return forest;
    }

private:
    TreeNode* dfs(TreeNode* node, bool isRoot, const std::unordered_set<int>& deleteSet,
                  std::vector<TreeNode*>& forest) {
        if (!node) {
            return nullptr;
        }
        bool removed = deleteSet.count(node->val) > 0;
        if (isRoot && !removed) {
            forest.push_back(node);
        }
        node->left = dfs(node->left, removed, deleteSet, forest);
        node->right = dfs(node->right, removed, deleteSet, forest);
        return removed ? nullptr : node;
    }
};
