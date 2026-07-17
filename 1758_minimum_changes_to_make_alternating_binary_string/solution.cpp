// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

#include <algorithm>
#include <string>

class Solution {
public:
    int minOperations(std::string s) {
        int n = (int)s.size();
        int alt1 = 0;
        for (int i = 0; i < n; i++) {
            char expected = (i & 1) == 0 ? '0' : '1';
            if (s[i] != expected) {
                alt1++;
            }
        }
        return std::min(alt1, n - alt1);
    }
};
