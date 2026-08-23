// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

public class Solution {
    public int ClimbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int prev = 1;
        int curr = 2;

        for (int i = 3; i <= n; i++) {
            int next = prev + curr;
            prev = curr;
            curr = next;
        }

        return curr;
    }
}
