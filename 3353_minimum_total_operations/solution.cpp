// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        int ops = 0;
        for (int i = (int)nums.size() - 2; i >= 0; i--) {
            if (nums[i] != nums[i + 1]) ops++;
        }
        return ops;
    }
};
