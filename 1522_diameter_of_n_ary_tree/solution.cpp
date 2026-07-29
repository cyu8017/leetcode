// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

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
    int diameter(Node* root) {
        answer_ = 0;
        if (root != nullptr) {
            depth(root);
        }
        return answer_;
    }

private:
    int answer_;

    int depth(Node* node) {
        int longest = 0;
        int second = 0;
        for (Node* child : node->children) {
            const int value = depth(child) + 1;
            if (value > longest) {
                second = longest;
                longest = value;
            } else if (value > second) {
                second = value;
            }
        }
        answer_ = std::max(answer_, longest + second);
        return longest;
    }
};
