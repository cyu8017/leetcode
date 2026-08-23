// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

#include <cstdint>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minLength(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int ans = n + 1, l = 0;
        std::unordered_map<int, int> cnt;
        int64_t s = 0;
        for (int r = 0; r < n; r++) {
            if (++cnt[nums[r]] == 1) s += nums[r];
            while (s >= k) {
                if (r - l + 1 < ans) ans = r - l + 1;
                if (--cnt[nums[l]] == 0) s -= nums[l];
                l++;
            }
        }
        return ans > n ? -1 : ans;
    }
};
