// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

public class Solution {
    public int[][] SpiralMatrix(int m, int n, ListNode head) {
        var ans = new int[m][];
        for (int i = 0; i < m; i++) {
            ans[i] = new int[n];
            for (int j = 0; j < n; j++) ans[i][j] = -1;
        }
        int[][] dirs = new int[][] { new[]{0,1}, new[]{1,0}, new[]{0,-1}, new[]{-1,0} };
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
            r = nr; c = nc;
        }
        return ans;
    }
}

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}
