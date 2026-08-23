// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

#include <vector>

class Solution {
public:
    long long subsequenceSumOr(std::vector<int>& nums) {
        long long ans = 0, prefix = 0;
        for (int x : nums) {
            prefix += x;
            ans |= (long long)x | prefix;
        }
        return ans;
    }
};
