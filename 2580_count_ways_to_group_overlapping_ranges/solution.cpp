// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countWays(std::vector<std::vector<int>>& ranges) {
        const int MOD = 1000000007;
        std::sort(ranges.begin(), ranges.end());
        int groups = 0, end = -1;
        for (auto& r : ranges) {
            if (r[0] > end) {
                groups++;
                end = r[1];
            } else if (r[1] > end) {
                end = r[1];
            }
        }
        int ans = 1;
        for (int i = 0; i < groups; ++i) ans = ans * 2 % MOD;
        return ans;
    }
};
