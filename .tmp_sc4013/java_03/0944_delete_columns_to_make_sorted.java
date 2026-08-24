// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution {
    public int minDeletionSize(String[] strs) {
        int ans = 0, m = strs[0].length(), n = strs.length;
        for (int c = 0; c < m; c++) {
            for (int r = 0; r + 1 < n; r++) {
                if (strs[r].charAt(c) > strs[r + 1].charAt(c)) { ans++; break; }
            }
        }
        return ans;
    }
}
