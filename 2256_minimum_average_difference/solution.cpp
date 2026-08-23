// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

#include <vector>
#include <cstdlib>
#include <climits>

class Solution {
public:
    int minimumAverageDifference(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long total = 0;
        for (int v : nums) total += v;
        long long left = 0, bestDiff = LLONG_MAX;
        int bestIdx = 0;
        for (int i = 0; i < n; ++i) {
            left += nums[i];
            long long leftAvg = left / (i + 1);
            long long rightAvg = 0;
            if (i != n - 1) rightAvg = (total - left) / (n - i - 1);
            long long diff = std::llabs(leftAvg - rightAvg);
            if (diff < bestDiff) { bestDiff = diff; bestIdx = i; }
        }
        return bestIdx;
    }
};
