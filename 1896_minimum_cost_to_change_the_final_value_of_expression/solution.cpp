// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

#include <algorithm>
#include <array>
#include <string>

class Solution {
public:
    int minOperationsToFlip(std::string expression) {
        expression_ = expression;
        index_ = 0;
        auto node = parseExpr();
        return node[0] ? node[1] : node[2];
    }

private:
    std::string expression_;
    int index_ = 0;

    using Node = std::array<int, 3>;

    Node combine(const Node& left, char op, const Node& right) {
        int leftVal = left[0], leftToZero = left[1], leftToOne = left[2];
        int rightVal = right[0], rightToZero = right[1], rightToOne = right[2];
        if (op == '&') {
            int andVal = leftVal & rightVal;
            int andToZero = std::min(leftToZero, leftToOne + rightToZero);
            int andToOne = leftToOne + rightToOne;
            int orToZero = leftToZero + rightToZero;
            int orToOne = std::min({leftToOne, leftToZero + rightToOne, rightToZero + leftToOne});
            return {andVal, std::min(andToZero, 1 + orToZero), std::min(andToOne, 1 + orToOne)};
        }
        int orVal = leftVal | rightVal;
        int orToZero = leftToZero + rightToZero;
        int orToOne = std::min({leftToOne, leftToZero + rightToOne, rightToZero + leftToOne});
        int andToZero = std::min(leftToZero, leftToOne + rightToZero);
        int andToOne = leftToOne + rightToOne;
        return {orVal, std::min(orToZero, 1 + andToZero), std::min(orToOne, 1 + andToOne)};
    }

    Node parseExpr() {
        Node node = parseFactor();
        while (index_ < static_cast<int>(expression_.size()) &&
               (expression_[index_] == '&' || expression_[index_] == '|')) {
            char op = expression_[index_++];
            node = combine(node, op, parseFactor());
        }
        return node;
    }

    Node parseFactor() {
        if (expression_[index_] == '0' || expression_[index_] == '1') {
            int value = expression_[index_++] - '0';
            return {value, value == 0 ? 0 : 1, value == 0 ? 1 : 0};
        }
        index_++;
        Node node = parseExpr();
        index_++;
        return node;
    }
};
