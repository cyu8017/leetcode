// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

#include <vector>

class Solution {
public:
    std::vector<int> concatWithReverse(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(2 * n);
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[n - i - 1];
        }
        return ans;
    }
};
