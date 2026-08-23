// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

#include <vector>

class Solution {
public:
    std::vector<int> applyOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        for (int i = 0; i + 1 < n; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        std::vector<int> ans(n);
        int j = 0;
        for (int x : nums) if (x != 0) ans[j++] = x;
        return ans;
    }
};
