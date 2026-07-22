// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

struct Node {
    int val;
    Node* left;
    Node* right;
    Node* parent;
    Node(int x) : val(x), left(nullptr), right(nullptr), parent(nullptr) {}
};

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node* q) {
        Node* a = p;
        Node* b = q;
        while (a != b) {
            a = a ? a->parent : q;
            b = b ? b->parent : p;
        }
        return a;
    }
};
