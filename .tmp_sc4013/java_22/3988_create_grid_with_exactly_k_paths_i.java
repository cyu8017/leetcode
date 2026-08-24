// CONFIG class=Solution method=solve types=None
// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] createGrid(int m, int n, int k) {
        List<String[]> cands = new ArrayList<>();
        if (k == 1) cands.add(new String[] { "." });
        else if (k == 2) cands.add(new String[] { "..", ".." });
        else if (k == 3) {
            cands.add(new String[] { "..", "..", ".." });
            cands.add(new String[] { "...", "..." });
        } else if (k == 4) {
            cands.add(new String[] { "..", "..", "..", ".." });
            cands.add(new String[] { "....", "...." });
            cands.add(new String[] { "..#", "...", "#.." });
        }
        for (String[] pat : cands) {
            int pr = pat.length, pc = pat[0].length();
            if (pr > m || pc > n) continue;
            String[] result = new String[m];
            for (int i = 0; i < m; i++) {
                char[] row = new char[n];
                java.util.Arrays.fill(row, '#');
                result[i] = new String(row);
            }
            for (int i = 0; i < pr; i++) {
                char[] row = result[i].toCharArray();
                for (int j = 0; j < pc; j++) row[j] = pat[i].charAt(j);
                result[i] = new String(row);
            }
            for (int i = pr; i < m; i++) {
                char[] row = result[i].toCharArray();
                row[pc - 1] = '.';
                result[i] = new String(row);
            }
            for (int j = pc; j < n; j++) {
                char[] row = result[m - 1].toCharArray();
                row[j] = '.';
                result[m - 1] = new String(row);
            }
            return result;
        }
        return new String[0];
    }
}
