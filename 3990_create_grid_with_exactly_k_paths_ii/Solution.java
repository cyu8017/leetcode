// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

class Solution {
    static int BitWidth(int k) {
        int w = 0;
        while (k != 0) { ++w; k >>= 1; }
        return w;
    }

    public String[] createGrid(int k) {
        if (k <= 0) return new String[0];
        int l = BitWidth((int)k);
        int m = 2 * l, n = l + 3;
        String[] result = new String[m];
        for (int i = 0; i < m; i++) {
            char[] row = new char[n];
            for (int j = 0; j < n; j++) row[j] = '#';
            result[i] = new String(row);
        }
        for (int i = 0; i < l; i++) {
            int r = 2 * i;
            char[] row0 = result[r].toCharArray();
            char[] row1 = result[r + 1].toCharArray();
            row0[i] = row0[i + 1] = row1[i] = row1[i + 1] = '.';
            if ((k & (1 << i)) != 0) {
                for (int c = i + 2; c < n; c++) row0[c] = '.';
            }
            result[r] = new String(row0);
            result[r + 1] = new String(row1);
        }
        for (int r = 0; r < m; r++) {
            char[] row = result[r].toCharArray();
            row[n - 1] = '.';
            result[r] = new String(row);
        }
        return result;
    }
}
