// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

#include <algorithm>
#include <string>

class Solution {
public:
    int minimumFlips(int n) {
        std::string s;
        long long x = n;
        if (x == 0) s = "0";
        else {
            while (x > 0) {
                s.push_back(char('0' + (x & 1)));
                x >>= 1;
            }
            std::reverse(s.begin(), s.end());
        }
        int m = (int)s.size(), cnt = 0;
        for (int i = 0; i < m / 2; i++) {
            if (s[i] != s[m - i - 1]) cnt++;
        }
        return cnt * 2;
    }
};
