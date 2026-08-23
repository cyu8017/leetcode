// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

#include <cctype>
#include <string>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    size_t index_ = 0;

    TreeNode* parse(const std::string& s) {
        if (index_ >= s.size()) {
            return nullptr;
        }

        int sign = 1;
        if (s[index_] == '-') {
            sign = -1;
            ++index_;
        }

        int value = 0;
        while (index_ < s.size() && std::isdigit(static_cast<unsigned char>(s[index_]))) {
            value = value * 10 + (s[index_] - '0');
            ++index_;
        }

        TreeNode* node = new TreeNode(sign * value);

        if (index_ < s.size() && s[index_] == '(') {
            ++index_;
            node->left = parse(s);
            ++index_;
        }

        if (index_ < s.size() && s[index_] == '(') {
            ++index_;
            node->right = parse(s);
            ++index_;
        }

        return node;
    }

public:
    TreeNode* str2tree(std::string s) {
        if (s.empty()) {
            return nullptr;
        }
        index_ = 0;
        return parse(s);
    }
};
