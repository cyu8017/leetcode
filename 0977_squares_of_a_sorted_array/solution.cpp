// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> sortedSquares(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n);
        int i = 0, j = n - 1;
        for (int k = n - 1; k >= 0; k--) {
            if (std::abs(nums[i]) > std::abs(nums[j])) {
                ans[k] = nums[i] * nums[i];
                i++;
            } else {
                ans[k] = nums[j] * nums[j];
                j--;
            }
        }
        return ans;
    }
};
