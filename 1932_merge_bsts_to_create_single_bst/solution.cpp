// LeetCode 1932 - Merge BSTs to Create Single BST
#include <climits>
#include <functional>
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
    TreeNode* canMerge(std::vector<TreeNode*>& trees) {
        std::unordered_map<int, TreeNode*> valueToRoot;
        std::unordered_map<int, int> count;
        for (TreeNode* tree : trees) {
            valueToRoot[tree->val] = tree;
            count[tree->val]++;
            if (tree->left) count[tree->left->val]++;
            if (tree->right) count[tree->right->val]++;
        }
        TreeNode* root = nullptr;
        int roots = 0;
        for (TreeNode* t : trees) {
            if (count[t->val] == 1) { root = t; roots++; }
        }
        if (roots != 1) return nullptr;
        valueToRoot.erase(root->val);
        std::function<bool(TreeNode*)> merge = [&](TreeNode* node) -> bool {
            if (!node) return true;
            if (node->left && valueToRoot.count(node->left->val)) {
                int v = node->left->val;
                node->left = valueToRoot[v];
                valueToRoot.erase(v);
            }
            if (node->right && valueToRoot.count(node->right->val)) {
                int v = node->right->val;
                node->right = valueToRoot[v];
                valueToRoot.erase(v);
            }
            return merge(node->left) && merge(node->right);
        };
        if (!merge(root) || !valueToRoot.empty()) return nullptr;
        std::function<bool(TreeNode*, long long, long long)> isValid = [&](TreeNode* node, long long lo, long long hi) -> bool {
            if (!node) return true;
            if (!(lo < node->val && node->val < hi)) return false;
            return isValid(node->left, lo, node->val) && isValid(node->right, node->val, hi);
        };
        return isValid(root, LLONG_MIN, LLONG_MAX) ? root : nullptr;
    }
};
