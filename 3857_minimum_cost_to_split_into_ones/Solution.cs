// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

public class Solution {
    public int MinCost(int n) {
        return n * (n - 1) / 2;
    }
}
