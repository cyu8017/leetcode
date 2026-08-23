// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

#include <vector>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int minK, int maxK) {
        long long ans = 0;
        int imin = -1, imax = -1, ibad = -1;
        for (int i = 0; i < (int)nums.size(); i++) {
            int x = nums[i];
            if (x < minK || x > maxK) ibad = i;
            if (x == minK) imin = i;
            if (x == maxK) imax = i;
            int bound = imin < imax ? imin : imax;
            if (bound > ibad) ans += bound - ibad;
        }
        return ans;
    }
};
