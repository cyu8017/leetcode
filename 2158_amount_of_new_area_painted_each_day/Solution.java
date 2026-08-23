// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

class Solution {
    public int[] amountPainted(int[][] paint) {
        int[] ans = new int[paint.length], line = new int[50001];
        for (int i = 0; i < paint.length; i++) {
            int start = paint[i][0], end = paint[i][1], j = start;
            while (j < end) {
                if (line[j] == 0) {
                    ans[i]++;
                    line[j] = end;
                    j++;
                } else {
                    int next = line[j];
                    line[j] = Math.max(end, next);
                    j = next;
                }
            }
        }
        return ans;
    }
}
