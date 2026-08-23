// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

#include <string>
#include <algorithm>

class Solution {
public:
    long long minimumCost(std::string s) {
        int n = (int)s.size();
        long long ans = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1]) ans += std::min(i, n - i);
        }
        return ans;
    }
};
