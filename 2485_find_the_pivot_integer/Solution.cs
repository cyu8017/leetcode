// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

public class Solution {
    public int PivotInteger(int n) {
        int total = n * (n + 1) / 2;
        int sum = 0;
        for (int x = 1; x <= n; x++) {
            sum += x;
            if (sum == total - sum + x) return x;
        }
        return -1;
    }
}
