// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

#include <string>

class Solution {
public:
    int countValidPrefixes(std::string s) {
        int ans = 0, t = 0;
        for (char c : s) {
            if (c == '1') t++;
            else t--;
            if (t >= -1 && t <= 1) ans++;
        }
        return ans;
    }
};
