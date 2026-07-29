// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

#include <string>

class Solution {
public:
    int minInsertions(std::string s) {
        int insertions = 0;
        int needed = 0;
        for (char ch : s) {
            if (ch == '(') {
                needed += 2;
                if (needed & 1) {
                    insertions += 1;
                    needed -= 1;
                }
            } else {
                needed -= 1;
                if (needed < 0) {
                    insertions += 1;
                    needed = 1;
                }
            }
        }
        return insertions + needed;
    }
};
