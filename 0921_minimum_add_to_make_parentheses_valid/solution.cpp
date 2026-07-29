// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

#include <string>

class Solution {
public:
    int minAddToMakeValid(std::string s) {
        int openNeed = 0, closeNeed = 0;
        for (char ch : s) {
            if (ch == '(') closeNeed++;
            else if (closeNeed) closeNeed--;
            else openNeed++;
        }
        return openNeed + closeNeed;
    }
};
