// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

public class Solution {
    public string[] CreateGrid(int m, int n) {
        string[] g = new string[m];
        for (int i = 0; i < m; i++) {
            char[] row = new char[n];
            for (int j = 0; j < n; j++) row[j] = '#';
            if (i == 0) for (int j = 0; j < n; j++) row[j] = '.';
            row[n - 1] = '.';
            g[i] = new string(row);
        }
        return g;
    }
}
