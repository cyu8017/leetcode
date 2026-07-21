// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    int minAbsoluteSumDiff(std::vector<int>& nums1, std::vector<int>& nums2) {
        const int MOD = 1000000007;
        std::vector<int> sortedNums1 = nums1;
        std::sort(sortedNums1.begin(), sortedNums1.end());
        long long total = 0;
        int bestGain = 0;
        int n = static_cast<int>(nums1.size());
        for (int i = 0; i < n; ++i) {
            int current = std::abs(nums1[i] - nums2[i]);
            total += current;
            int target = nums2[i];
            auto it = std::lower_bound(sortedNums1.begin(), sortedNums1.end(), target);
            if (it != sortedNums1.end()) {
                bestGain = std::max(bestGain, current - std::abs(*it - target));
            }
            if (it != sortedNums1.begin()) {
                --it;
                bestGain = std::max(bestGain, current - std::abs(*it - target));
            }
        }
        return static_cast<int>((total - bestGain) % MOD);
    }
};
