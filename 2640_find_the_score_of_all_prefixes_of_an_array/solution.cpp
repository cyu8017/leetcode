// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

#include <vector>

class Solution {
public:
    std::vector<long long> findPrefixScore(std::vector<int>& nums) {
        std::vector<long long> ans(nums.size());
        int mx = 0;
        long long sum = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] > mx) mx = nums[i];
            sum += nums[i] + mx;
            ans[i] = sum;
        }
        return ans;
    }
};
