// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestEqualSubarray(std::vector<int>& nums, int k) {
        std::unordered_map<int, std::vector<int>> pos;
        for (int i = 0; i < (int)nums.size(); i++) pos[nums[i]].push_back(i);
        int ans = 0;
        for (auto& [_, p] : pos) {
            int left = 0;
            for (int right = 0; right < (int)p.size(); right++) {
                while (p[right] - p[left] - (right - left) > k) left++;
                ans = std::max(ans, right - left + 1);
            }
        }
        return ans;
    }
};
