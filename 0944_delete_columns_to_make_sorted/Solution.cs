// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

public class Solution {
    public int MinDeletionSize(string[] strs) {
        int ans = 0, m = strs[0].Length, n = strs.Length;
        for (int c = 0; c < m; c++) {
            for (int r = 0; r + 1 < n; r++) {
                if (strs[r][c] > strs[r + 1][c]) { ans++; break; }
            }
        }
        return ans;
    }
}
