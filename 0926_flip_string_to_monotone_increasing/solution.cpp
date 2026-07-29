// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

#include <algorithm>
#include <string>

class Solution {
public:
    int minFlipsMonoIncr(std::string s) {
        int ones = 0, ans = 0;
        for (char ch : s) {
            if (ch == '1') ones++;
            else ans = std::min(ans + 1, ones);
        }
        return ans;
    }
};
