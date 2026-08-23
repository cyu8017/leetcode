// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution {
    public int maximumGroups(int[] grades) {
        int n = grades.length;
        int k = 0;
        while ((k + 1L) * (k + 2) / 2 <= n) k++;
        return k;
    }
}
