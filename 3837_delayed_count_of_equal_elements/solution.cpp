// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> delayedCount(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::unordered_map<int, int> cnt;
        std::vector<int> ans(n, 0);
        for (int i = n - k - 2; i >= 0; i--) {
            cnt[nums[i + k + 1]]++;
            ans[i] = cnt[nums[i]];
        }
        return ans;
    }
};
