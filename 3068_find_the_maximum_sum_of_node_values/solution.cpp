// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maximumValueSum(std::vector<int>& nums, int k, std::vector<std::vector<int>>& edges) {
        (void)edges;
        long long f0 = 0, f1 = -0x3f3f3f3fLL;
        for (int x : nums) {
            long long nf0 = std::max(f0 + x, f1 + (x ^ k));
            long long nf1 = std::max(f1 + x, f0 + (x ^ k));
            f0 = nf0;
            f1 = nf1;
        }
        return f0;
    }
};
