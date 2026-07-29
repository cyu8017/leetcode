// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

#include <stack>
#include <string>
#include <unordered_map>

class Node {
public:
    char val;
    Node* left;
    Node* right;
    Node() : val(' '), left(nullptr), right(nullptr) {}
    Node(char x) : val(x), left(nullptr), right(nullptr) {}
    Node(char x, Node* left, Node* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    Node* expTree(std::string s) {
        std::stack<Node*> nodes;
        std::stack<char> ops;
        const std::unordered_map<char, int> priority{{'+', 1}, {'-', 1}, {'*', 2}, {'/', 2}};
        auto apply = [&]() {
            const char op = ops.top();
            ops.pop();
            Node* right = nodes.top();
            nodes.pop();
            Node* left = nodes.top();
            nodes.pop();
            nodes.push(new Node(op, left, right));
        };
        for (char ch : s) {
            if (ch >= '0' && ch <= '9') {
                nodes.push(new Node(ch));
            } else if (ch == '(') {
                ops.push(ch);
            } else if (ch == ')') {
                while (ops.top() != '(') {
                    apply();
                }
                ops.pop();
            } else {
                while (!ops.empty() && ops.top() != '(' &&
                       priority.at(ops.top()) >= priority.at(ch)) {
                    apply();
                }
                ops.push(ch);
            }
        }
        while (!ops.empty()) {
            apply();
        }
        return nodes.top();
    }
};
