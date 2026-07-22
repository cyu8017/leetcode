// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

#include <array>
#include <sstream>
#include <string>
#include <vector>

struct Node {
    char val;
    Node* left;
    Node* right;
    Node(char v = 0) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
    static Node* parse(const std::string& data) {
        if (data.empty() || data == "[]") {
            return nullptr;
        }
        std::string inner = data;
        if (inner.front() == '[') {
            inner = inner.substr(1, inner.size() - 2);
        }
        std::vector<std::string> vals;
        std::stringstream ss(inner);
        std::string item;
        while (std::getline(ss, item, ',')) {
            vals.push_back(item);
        }
        std::vector<Node*> nodes;
        nodes.reserve(vals.size());
        for (const auto& x : vals) {
            if (x == "null") {
                nodes.push_back(nullptr);
            } else {
                nodes.push_back(new Node(x.empty() ? 0 : x[0]));
            }
        }
        size_t kid = 1;
        for (Node* node : nodes) {
            if (!node) {
                continue;
            }
            if (kid < nodes.size()) {
                node->left = nodes[kid++];
            }
            if (kid < nodes.size()) {
                node->right = nodes[kid++];
            }
        }
        return nodes.empty() ? nullptr : nodes[0];
    }

    static void countLetters(Node* node, std::array<int, 26>& cnt) {
        if (!node) {
            return;
        }
        if (node->val == '+') {
            countLetters(node->left, cnt);
            countLetters(node->right, cnt);
        } else {
            ++cnt[node->val - 'a'];
        }
    }

public:
    bool checkEquivalence(std::string root1, std::string root2) {
        Node* a = parse(root1);
        Node* b = parse(root2);
        std::array<int, 26> ca{}, cb{};
        countLetters(a, ca);
        countLetters(b, cb);
        return ca == cb;
    }
};
