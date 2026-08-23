// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

#include <string>

class Solution {
public:
    bool canMakeSubsequence(std::string s, std::string t) {
        int m = (int)s.size();
        int n = (int)t.size();
        int i0 = 0, i1 = 0, j = 0;
        while (i1 < m && j < n) {
            if (s[i1] == t[j]) i1++;
            if (i1 < i0 + 1) i1 = i0 + 1;
            if (s[i0] == t[j]) i0++;
            j++;
        }
        return i1 == m;
    }
};
