// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

#include <cctype>
#include <string>

class Solution {
public:
    std::string makeGood(std::string s) {
        std::string stack;
        for (char ch : s) {
            if (!stack.empty() && stack.back() != ch &&
                std::tolower(static_cast<unsigned char>(stack.back())) ==
                    std::tolower(static_cast<unsigned char>(ch))) {
                stack.pop_back();
            } else {
                stack.push_back(ch);
            }
        }
        return stack;
    }
};
