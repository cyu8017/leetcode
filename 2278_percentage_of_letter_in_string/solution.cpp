// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

#include <string>

class Solution {
public:
    int percentageLetter(std::string s, char letter) {
        int cnt = 0;
        for (char c : s) if (c == letter) cnt++;
        return cnt * 100 / (int)s.size();
    }
};
