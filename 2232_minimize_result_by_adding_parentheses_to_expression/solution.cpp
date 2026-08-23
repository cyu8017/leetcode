// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

#include <string>
#include <climits>

class Solution {
public:
    std::string minimizeResult(std::string expression) {
        size_t plus = expression.find('+');
        std::string left = expression.substr(0, plus);
        std::string right = expression.substr(plus + 1);
        int bestVal = INT_MAX;
        std::string best;
        for (size_t i = 0; i < left.size(); ++i) {
            for (size_t j = 1; j <= right.size(); ++j) {
                std::string a = left.substr(0, i);
                std::string b = left.substr(i);
                std::string c = right.substr(0, j);
                std::string d = right.substr(j);
                int val = std::stoi(b) + std::stoi(c);
                if (!a.empty()) val *= std::stoi(a);
                if (!d.empty()) val *= std::stoi(d);
                std::string cand = a + "(" + b + "+" + c + ")" + d;
                if (val < bestVal) {
                    bestVal = val;
                    best = cand;
                }
            }
        }
        return best;
    }
};
