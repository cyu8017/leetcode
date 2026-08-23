// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
    public int minCost(int n) {
        return n * (n - 1) / 2;
    }
}
