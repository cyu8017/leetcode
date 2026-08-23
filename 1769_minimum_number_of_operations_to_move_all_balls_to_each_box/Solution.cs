// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

public class Solution {
    public int[] MinOperations(string boxes) {
        int n = boxes.Length;
        int[] ans = new int[n];
        int balls = 0;
        int ops = 0;
        for (int i = 1; i < n; i++) {
            balls += boxes[i - 1] - '0';
            ops += balls;
            ans[i] = ops;
        }
        balls = 0;
        ops = 0;
        for (int i = n - 2; i >= 0; i--) {
            balls += boxes[i + 1] - '0';
            ops += balls;
            ans[i] += ops;
        }
        return ans;
    }
}
