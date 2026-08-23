// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

public class Solution {
    public int[] AmountPainted(int[][] paint) {
        int[] ans = new int[paint.Length], line = new int[50001];
        for (int i = 0; i < paint.Length; i++) {
            int start = paint[i][0], end = paint[i][1], j = start;
            while (j < end) {
                if (line[j] == 0) {
                    ans[i]++;
                    line[j] = end;
                    j++;
                } else {
                    int next = line[j];
                    line[j] = Math.Max(end, next);
                    j = next;
                }
            }
        }
        return ans;
    }
}
