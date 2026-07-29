// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int kthSmallestSubarraySum(std::vector<int>& nums, int k) {
        auto count = [&](int limit) {
            long long total = 0;
            int left = 0, ans = 0;
            for (int right = 0; right < (int)nums.size(); right++) {
                total += nums[right];
                while (total > limit) total -= nums[left++];
                ans += right - left + 1;
            }
            return ans;
        };
        int lo = *std::min_element(nums.begin(), nums.end());
        int hi = std::accumulate(nums.begin(), nums.end(), 0);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (count(mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
