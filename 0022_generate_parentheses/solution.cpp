// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

#include <string>
#include <vector>

class Solution {
    void backtrack(
        std::vector<std::string>& result,
        std::string& path,
        int n,
        int openCount,
        int closeCount
    ) {
        if (static_cast<int>(path.size()) == 2 * n) {
            result.push_back(path);
            return;
        }
        if (openCount < n) {
            path.push_back('(');
            backtrack(result, path, n, openCount + 1, closeCount);
            path.pop_back();
        }
        if (closeCount < openCount) {
            path.push_back(')');
            backtrack(result, path, n, openCount, closeCount + 1);
            path.pop_back();
        }
    }

public:
    std::vector<std::string> generateParenthesis(int n) {
        std::vector<std::string> result;
        std::string path;
        backtrack(result, path, n, 0, 0);
        return result;
    }
};
