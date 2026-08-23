// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

#include <algorithm>
#include <cstdint>
#include <string>

class Solution {
public:
    long long minimumCost(std::string s, std::string t, int flipCost, int swapCost, int crossCost) {
        int64_t diff[2] = {0, 0};
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            if (s[i] != t[i]) diff[s[i] - '0']++;
        }
        int64_t ans = (diff[0] + diff[1]) * flipCost;
        int64_t mx = std::max(diff[0], diff[1]);
        int64_t mn = std::min(diff[0], diff[1]);
        ans = std::min(ans, mn * swapCost + (mx - mn) * flipCost);
        int64_t avg = (mx + mn) / 2;
        ans = std::min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost);
        return ans;
    }
};
