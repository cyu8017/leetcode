// LeetCode 3958 - Minimum Cost To Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

class Solution {
public:
    long long minCost(int n) {
        return 1LL * n * (n - 1) / 2;
    }
};
