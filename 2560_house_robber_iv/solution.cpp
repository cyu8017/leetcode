// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCapability(std::vector<int>& nums, int k) {
        int lo = *std::min_element(nums.begin(), nums.end());
        int hi = *std::max_element(nums.begin(), nums.end());
        auto ok = [&](int cap) {
            int cnt = 0;
            for (int i = 0; i < (int)nums.size();) {
                if (nums[i] <= cap) {
                    cnt++;
                    i += 2;
                } else {
                    i++;
                }
            }
            return cnt >= k;
        };
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
