// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

#include <string>

class Solution {
public:
    bool halvesAreAlike(std::string s) {
        const std::string vowels = "aeiouAEIOU";
        int mid = static_cast<int>(s.size()) / 2;
        int balance = 0;
        for (int i = 0; i < static_cast<int>(s.size()); i++) {
            if (vowels.find(s[i]) != std::string::npos) {
                balance += i < mid ? 1 : -1;
            }
        }
        return balance == 0;
    }
};
