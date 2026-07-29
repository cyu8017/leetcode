// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

#include <string>

class Solution {
public:
    bool isDecomposable(std::string s) {
        int n = (int)s.size(), i = 0, twos = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            int length = j - i;
            if (length % 3 == 1) return false;
            if (length % 3 == 2) {
                if (++twos > 1) return false;
            }
            i = j;
        }
        return twos == 1;
    }
};
