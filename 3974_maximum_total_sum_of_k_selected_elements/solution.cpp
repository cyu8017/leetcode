// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int k, int mul) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = n - 1; i >= n - k; i--) {
            int m = std::max(1, mul);
            ans += (long long)nums[i] * m;
            mul--;
        }
        return ans;
    }
};
