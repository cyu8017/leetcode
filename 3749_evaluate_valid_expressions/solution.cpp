// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

#include <cctype>
#include <functional>
#include <string>
#include <utility>

class Solution {
public:
    long long evaluateExpression(std::string expression) {
        std::function<std::pair<long long, int>(int)> parse = [&](int i) -> std::pair<long long, int> {
            if (std::isdigit(expression[i]) || expression[i] == '-') {
                int j = i;
                if (expression[j] == '-') j++;
                while (j < (int)expression.size() && std::isdigit(expression[j])) j++;
                return {std::stoll(expression.substr(i, j - i)), j};
            }
            int j = i;
            while (expression[j] != '(') j++;
            std::string op = expression.substr(i, j - i);
            j++;
            auto [val1, nextJ1] = parse(j);
            j = nextJ1 + 1;
            auto [val2, nextJ2] = parse(j);
            j = nextJ2 + 1;
            long long res = 0;
            if (op == "add") res = val1 + val2;
            else if (op == "sub") res = val1 - val2;
            else if (op == "mul") res = val1 * val2;
            else if (op == "div") res = val1 / val2;
            return {res, j};
        };
        return parse(0).first;
    }
};
