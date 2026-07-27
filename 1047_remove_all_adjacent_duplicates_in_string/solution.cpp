// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

#include <string>

class Solution {
public:
    std::string removeDuplicates(std::string s) {
        std::string stack;
        for (char ch : s) {
            if (!stack.empty() && stack.back() == ch) stack.pop_back();
            else stack.push_back(ch);
        }
        return stack;
    }
};

