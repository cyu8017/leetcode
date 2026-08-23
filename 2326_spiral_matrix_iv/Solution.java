// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                ans[i][j] = -1;
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int r = 0, c = 0, d = 0;
        while (head != null) {
            ans[r][c] = head.val;
            head = head.next;
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1) {
                d = (d + 1) % 4;
                nr = r + dirs[d][0];
                nc = c + dirs[d][1];
            }
            r = nr;
            c = nc;
        }
        return ans;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
