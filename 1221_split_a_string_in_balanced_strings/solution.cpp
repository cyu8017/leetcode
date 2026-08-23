// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

#include <string>

class Solution {
public:
    int balancedStringSplit(std::string s) {
        int balance = 0, answer = 0;
        for (char ch : s) {
            balance += (ch == 'L') ? 1 : -1;
            if (balance == 0) {
                ++answer;
            }
        }
        return answer;
    }
};
