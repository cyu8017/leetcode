// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

public class Solution {
    public int[] RowAndMaximumOnes(int[][] mat) {
        int bestRow = 0, bestCnt = -1;
        for (int i = 0; i < mat.Length; i++) {
            int cnt = 0;
            foreach (int v in mat[i]) cnt += v;
            if (cnt > bestCnt) { bestCnt = cnt; bestRow = i; }
        }
        return new int[] { bestRow, bestCnt };
    }
}
