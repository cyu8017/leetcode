// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

#include <vector>

class Solution {
public:
    int minimumCost(std::vector<int>& nums) {
        int a = nums[0], b = 100, c = 100;
        for (int i = 1; i < (int)nums.size(); i++) {
            int x = nums[i];
            if (x < b) {
                c = b;
                b = x;
            } else if (x < c) {
                c = x;
            }
        }
        return a + b + c;
    }
};
