// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        int ans = 0, cur = 0, l = 0;
        for (int r = 0; r < (int)nums.size(); r++) {
            if (++cnt[nums[r]] == 2) cur++;
            while (cur > k) {
                if (--cnt[nums[l]] == 1) cur--;
                l++;
            }
            ans = std::max(ans, r - l + 1);
        }
        return ans;
    }
};
