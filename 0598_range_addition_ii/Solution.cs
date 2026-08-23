// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/

public class Solution {
    public int MaxCount(int m, int n, int[][] ops) {
        foreach (int[] op in ops) {
            if (op[0] < m) m = op[0];
            if (op[1] < n) n = op[1];
        }
        return m * n;
    }
}
