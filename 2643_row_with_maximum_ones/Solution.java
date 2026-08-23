// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int bestRow = 0, bestCnt = -1;
        for (int i = 0; i < mat.length; i++) {
            int cnt = 0;
            for (int v : mat[i]) cnt += v;
            if (cnt > bestCnt) {
                bestCnt = cnt;
                bestRow = i;
            }
        }
        return new int[] {bestRow, bestCnt};
    }
}
