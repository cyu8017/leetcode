// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long countNonDecreasingSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long cost = 0;
            int maxV = nums[i];
            for (int j = i; j < n; j++) {
                if (nums[j] >= maxV) maxV = nums[j];
                else cost += maxV - nums[j];
                if (cost > k) break;
                ans++;
            }
        }
        return ans;
    }
};
