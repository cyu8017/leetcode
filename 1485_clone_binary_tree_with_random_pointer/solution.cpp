#include <unordered_map>

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* random;
    Node() : val(0), left(nullptr), right(nullptr), random(nullptr) {}
    Node(int _val) : val(_val), left(nullptr), right(nullptr), random(nullptr) {}
};

class Solution {
    std::unordered_map<Node*, Node*> copies;
    Node* clone(Node* node) {
        if (!node) return nullptr;
        if (!copies.count(node)) {
            copies[node] = new Node(node->val);
            copies[node]->left = clone(node->left);
            copies[node]->right = clone(node->right);
            copies[node]->random = clone(node->random);
        }
        return copies[node];
    }
public:
    Node* copyRandomBinaryTree(Node* root) {
        return clone(root);
    }
};
