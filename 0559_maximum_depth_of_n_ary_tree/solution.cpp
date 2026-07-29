// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

#include <algorithm>
#include <vector>

class Node {
public:
    int val;
    std::vector<Node*> children;
    Node() : val(0) {}
    explicit Node(int _val) : val(_val) {}
    Node(int _val, std::vector<Node*> _children) : val(_val), children(std::move(_children)) {}
};

class Solution {
public:
    int maxDepth(Node* root) {
        if (root == nullptr) {
            return 0;
        }
        if (root->children.empty()) {
            return 1;
        }
        int best = 0;
        for (Node* child : root->children) {
            best = std::max(best, maxDepth(child));
        }
        return best + 1;
    }
};
