// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution {
    public int minDeletionSize(String[] strs) {
        int n = strs.length, m = strs[0].length(), deleted = 0;
        boolean[] sortedPair = new boolean[n - 1];
        for (int c = 0; c < m; c++) {
            boolean bad = false;
            for (int r = 0; r + 1 < n; r++) {
                if (!sortedPair[r] && strs[r].charAt(c) > strs[r + 1].charAt(c)) { bad = true; break; }
            }
            if (bad) { deleted++; continue; }
            for (int r = 0; r + 1 < n; r++)
                if (strs[r].charAt(c) < strs[r + 1].charAt(c)) sortedPair[r] = true;
        }
        return deleted;
    }
}
