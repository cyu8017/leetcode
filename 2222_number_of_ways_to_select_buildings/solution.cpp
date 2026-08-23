// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

#include <string>

class Solution {
public:
    long long numberOfWays(std::string s) {
        int n = (int)s.size();
        int total0 = 0, total1 = 0;
        for (char c : s) {
            if (c == '0') total0++;
            else total1++;
        }
        int left0 = 0, left1 = 0;
        long long ans = 0;
        for (char c : s) {
            if (c == '0') {
                ans += 1LL * left1 * (total1 - left1);
                left0++;
            } else {
                ans += 1LL * left0 * (total0 - left0);
                left1++;
            }
        }
        return ans;
    }
};
