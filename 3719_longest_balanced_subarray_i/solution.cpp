// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int longestBalanced(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> vis;
            int cnt[2] = {};
            for (int j = i; j < n; j++) {
                if (!vis.count(nums[j])) {
                    vis.insert(nums[j]);
                    cnt[nums[j] & 1]++;
                }
                if (cnt[0] == cnt[1]) ans = std::max(ans, j - i + 1);
            }
        }
        return ans;
    }
};
