// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

#include <vector>

class Solution {
public:
    int maxIncreasingSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> up(n);
        up[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            up[i] = (nums[i] < nums[i + 1]) ? up[i + 1] + 1 : 1;
        }
        int lo = 1, hi = n / 2;
        auto ok = [&](int k) {
            for (int i = 0; i + 2 * k <= n; i++) {
                if (up[i] >= k && up[i + k] >= k) return true;
            }
            return false;
        };
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
