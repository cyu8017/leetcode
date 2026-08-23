// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

#include <string>

class Solution {
public:
    std::string removeOccurrences(std::string s, std::string part) {
        std::string stack;
        int m = (int)part.size();
        for (char ch : s) {
            stack.push_back(ch);
            if ((int)stack.size() >= m && stack.compare(stack.size() - m, m, part) == 0) {
                stack.erase(stack.size() - m);
            }
        }
        return stack;
    }
};
