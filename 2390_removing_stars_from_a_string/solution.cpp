// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

#include <string>

class Solution {
public:
    std::string removeStars(std::string s) {
        std::string stack;
        for (char c : s) {
            if (c == '*') stack.pop_back();
            else stack.push_back(c);
        }
        return stack;
    }
};
