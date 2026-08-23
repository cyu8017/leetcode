// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

#include <stack>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class BSTIterator {
    std::vector<int> values;
    int index;

public:
    BSTIterator(TreeNode* root) : index(-1) {
        std::stack<TreeNode*> stack;
        while (!stack.empty() || root) {
            while (root) {
                stack.push(root);
                root = root->left;
            }
            root = stack.top();
            stack.pop();
            values.push_back(root->val);
            root = root->right;
        }
    }

    bool hasNext() {
        return index + 1 < static_cast<int>(values.size());
    }

    int next() {
        ++index;
        return values[index];
    }

    bool hasPrev() {
        return index > 0;
    }

    int prev() {
        --index;
        return values[index];
    }
};
