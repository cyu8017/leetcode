// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

#include <string>

class Solution {
public:
    long long countSubstrings(std::string s, char c) {
        long long cnt = 0;
        for (char ch : s) if (ch == c) cnt++;
        return cnt + cnt * (cnt - 1) / 2;
    }
};
