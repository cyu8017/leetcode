// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> answerQueries(std::vector<int>& nums, std::vector<int>& queries) {
        std::sort(nums.begin(), nums.end());
        for (int i = 1; i < (int)nums.size(); i++) nums[i] += nums[i - 1];
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            ans[i] = (int)(std::upper_bound(nums.begin(), nums.end(), queries[i]) - nums.begin());
        }
        return ans;
    }
};
