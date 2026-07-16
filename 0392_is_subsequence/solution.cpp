// LeetCode 0392 - Is Subsequence
// https://leetcode.com/problems/is-subsequence/

#include <string>

class Solution {
public:
    bool isSubsequence(std::string s, std::string t) {
        int index = 0;
        for (char ch : t) {
            if (index < static_cast<int>(s.size()) && s[index] == ch) {
                index += 1;
            }
        }
        return index == static_cast<int>(s.size());
    }
};
