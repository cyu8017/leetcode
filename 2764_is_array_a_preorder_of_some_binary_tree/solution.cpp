// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

#include <vector>

class Solution {
public:
    bool isPreorder(std::vector<std::vector<int>>& nodes) {
        if (nodes.empty()) return true;
        std::vector<int> stack;
        stack.push_back(nodes[0][0]);
        for (int i = 1; i < (int)nodes.size(); i++) {
            int id = nodes[i][0], parent = nodes[i][1];
            while (!stack.empty() && stack.back() != parent) stack.pop_back();
            if (stack.empty()) return false;
            stack.push_back(id);
        }
        return true;
    }
};
