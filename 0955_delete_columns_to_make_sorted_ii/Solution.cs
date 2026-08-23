// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

public class Solution {
    public int MinDeletionSize(string[] strs) {
        int n = strs.Length, m = strs[0].Length, deleted = 0;
        bool[] sortedPair = new bool[n - 1];
        for (int c = 0; c < m; c++) {
            bool bad = false;
            for (int r = 0; r + 1 < n; r++) {
                if (!sortedPair[r] && strs[r][c] > strs[r + 1][c]) { bad = true; break; }
            }
            if (bad) { deleted++; continue; }
            for (int r = 0; r + 1 < n; r++)
                if (strs[r][c] < strs[r + 1][c]) sortedPair[r] = true;
        }
        return deleted;
    }
}
