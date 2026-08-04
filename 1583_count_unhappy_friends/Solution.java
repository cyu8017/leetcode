// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

class Solution {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[][] rank = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rank[i][preferences[i][j]] = j;
            }
        }
        int[] partner = new int[n];
        for (int[] p : pairs) {
            partner[p[0]] = p[1];
            partner[p[1]] = p[0];
        }
        int unhappy = 0;
        for (int x = 0; x < n; x++) {
            int y = partner[x];
            for (int k = 0; k < rank[x][y]; k++) {
                int u = preferences[x][k];
                if (rank[u][x] < rank[u][partner[u]]) {
                    unhappy++;
                    break;
                }
            }
        }
        return unhappy;
    }
}
