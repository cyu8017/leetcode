// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

#include <cctype>
#include <string>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* recoverFromPreorder(std::string traversal) {
        std::vector<TreeNode*> stack;
        int i = 0, n = static_cast<int>(traversal.size());
        while (i < n) {
            int depth = 0;
            while (i < n && traversal[i] == '-') {
                ++depth;
                ++i;
            }
            int start = i;
            while (i < n && std::isdigit(static_cast<unsigned char>(traversal[i]))) ++i;
            TreeNode* node = new TreeNode(std::stoi(traversal.substr(start, i - start)));
            while (static_cast<int>(stack.size()) > depth) stack.pop_back();
            if (!stack.empty()) {
                if (!stack.back()->left) stack.back()->left = node;
                else stack.back()->right = node;
            }
            stack.push_back(node);
        }
        return stack[0];
    }
};

