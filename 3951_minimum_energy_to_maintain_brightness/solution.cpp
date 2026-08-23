// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minEnergy(int n, int brightness, std::vector<std::vector<int>>& intervals) {
        (void)n;
        std::sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
            return a[0] < b[0];
        });
        std::vector<std::vector<int>> merged = {intervals[0]};
        for (int i = 1; i < (int)intervals.size(); i++) {
            auto& x = intervals[i];
            if (merged.back()[1] < x[0]) merged.push_back(x);
            else if (x[1] > merged.back()[1]) merged.back()[1] = x[1];
        }
        long long ans = 0;
        for (auto& interval : merged) {
            int m = interval[1] - interval[0] + 1;
            ans += (long long)((brightness + 2) / 3) * m;
        }
        return ans;
    }
};
