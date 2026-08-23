// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> maxKDistinct(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<int> ans;
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n && nums[i] == nums[i + 1]) continue;
            ans.push_back(nums[i]);
            if (--k == 0) break;
        }
        return ans;
    }
};
