// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

class Solution {
    public int minOperations(String initial, String target) {
        int m = initial.length(), n = target.length();
        int[][] f = new int[m + 1][];
        for (int i = 0; i <= m; i++) f[i] = new int[n + 1];
        int mx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (initial.charAt(i) == target.charAt(j)) {
                    f[i + 1][j + 1] = f[i][j] + 1;
                    mx = Math.max(mx, f[i + 1][j + 1]);
                }
            }
        }
        return m + n - 2 * mx;
    }
}
