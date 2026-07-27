// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

#include <string>
#include <vector>

class Solution {
public:
    bool isValid(std::string s) {
        std::vector<char> stack;
        for (char ch : s) {
            stack.push_back(ch);
            int n = static_cast<int>(stack.size());
            if (n >= 3 && stack[n - 3] == 'a' && stack[n - 2] == 'b' && stack[n - 1] == 'c') {
                stack.pop_back();
                stack.pop_back();
                stack.pop_back();
            }
        }
        return stack.empty();
    }
};

