// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

#include <cctype>
#include <set>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> braceExpansionII(std::string expression) {
        int i = 0;
        auto result = parse(expression, i);
        return std::vector<std::string>(result.begin(), result.end());
    }

private:
    std::set<std::string> parse(const std::string& expr, int& i) {
        std::set<std::string> unionSet;
        std::set<std::string> cur = {""};
        while (i < static_cast<int>(expr.size()) && expr[i] != '}') {
            if (expr[i] == '{') {
                ++i;
                auto nested = parse(expr, i);
                std::set<std::string> next;
                for (const auto& a : cur) {
                    for (const auto& b : nested) {
                        next.insert(a + b);
                    }
                }
                cur.swap(next);
            } else if (expr[i] == ',') {
                unionSet.insert(cur.begin(), cur.end());
                cur = {""};
                ++i;
            } else {
                int j = i;
                while (j < static_cast<int>(expr.size()) && std::isalpha(static_cast<unsigned char>(expr[j]))) {
                    ++j;
                }
                std::string token = expr.substr(i, j - i);
                std::set<std::string> next;
                for (const auto& a : cur) {
                    next.insert(a + token);
                }
                cur.swap(next);
                i = j;
            }
        }
        unionSet.insert(cur.begin(), cur.end());
        ++i;
        return unionSet;
    }
};
