// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

public class Solution {
    static int BitWidth(uint k) {
        int w = 0;
        while (k != 0) { ++w; k >>= 1; }
        return w;
    }

    public string[] CreateGrid(int k) {
        if (k <= 0) return new string[0];
        int l = BitWidth((uint)k);
        int m = 2 * l, n = l + 3;
        string[] result = new string[m];
        for (int i = 0; i < m; i++) {
            char[] row = new char[n];
            for (int j = 0; j < n; j++) row[j] = '#';
            result[i] = new string(row);
        }
        for (int i = 0; i < l; i++) {
            int r = 2 * i;
            char[] row0 = result[r].ToCharArray();
            char[] row1 = result[r + 1].ToCharArray();
            row0[i] = row0[i + 1] = row1[i] = row1[i + 1] = '.';
            if ((k & (1 << i)) != 0) {
                for (int c = i + 2; c < n; c++) row0[c] = '.';
            }
            result[r] = new string(row0);
            result[r + 1] = new string(row1);
        }
        for (int r = 0; r < m; r++) {
            char[] row = result[r].ToCharArray();
            row[n - 1] = '.';
            result[r] = new string(row);
        }
        return result;
    }
}
