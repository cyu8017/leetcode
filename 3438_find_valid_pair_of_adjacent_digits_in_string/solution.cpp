// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

#include <string>

class Solution {
public:
    std::string findValidPair(std::string s) {
        int freq[10] = {};
        for (char c : s) freq[c - '0']++;
        for (int i = 0; i + 1 < (int)s.size(); i++) {
            int a = s[i] - '0', b = s[i + 1] - '0';
            if (a != b && freq[a] == a && freq[b] == b) return s.substr(i, 2);
        }
        return "";
    }
};
