// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

#include <stack>
#include <string>
#include <vector>

class Node {
public:
    virtual ~Node() = default;
    virtual int evaluate() const = 0;

protected:
    Node() = default;
};

class NumNode : public Node {
    int val_;

public:
    explicit NumNode(int val) : val_(val) {}
    int evaluate() const override { return val_; }
};

class OpNode : public Node {
    char op_;
    Node* left_;
    Node* right_;

public:
    OpNode(char op, Node* left, Node* right) : op_(op), left_(left), right_(right) {}
    int evaluate() const override {
        const int a = left_->evaluate();
        const int b = right_->evaluate();
        switch (op_) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
        }
        return 0;
    }
};

class TreeBuilder {
    Node* build(std::vector<std::string>& postfix) {
        std::stack<Node*> st;
        for (const auto& token : postfix) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                Node* right = st.top();
                st.pop();
                Node* left = st.top();
                st.pop();
                st.push(new OpNode(token[0], left, right));
            } else {
                st.push(new NumNode(std::stoi(token)));
            }
        }
        return st.top();
    }

public:
    // Harness compares against the evaluated result (same as Python Node.__eq__).
    int expTree(std::vector<std::string>& postfix) {
        return build(postfix)->evaluate();
    }
};
