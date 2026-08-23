// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

#include <numeric>
#include <vector>

class Solution {
public:
    int subarrayLCM(std::vector<int>& nums, int k) {
        int ans = 0, n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            long long cur = 1;
            for (int j = i; j < n; j++) {
                cur = cur / std::gcd((int)cur, nums[j]) * nums[j];
                if (cur > k) break;
                if (cur == k) ans++;
            }
        }
        return ans;
    }
};
