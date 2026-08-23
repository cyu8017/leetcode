// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, std::vector<int>& numsDivide) {
        int g = numsDivide[0];
        for (int i = 1; i < (int)numsDivide.size(); i++) {
            g = std::gcd(g, numsDivide[i]);
        }
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < (int)nums.size(); i++) {
            if (g % nums[i] == 0) return i;
        }
        return -1;
    }
};
