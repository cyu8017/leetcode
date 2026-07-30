// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

public class Solution {
    public int UnhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[][] rank = new int[n][];
        for (int i = 0; i < n; i++) {
            rank[i] = new int[n];
            for (int j = 0; j < preferences[i].Length; j++)
                rank[i][preferences[i][j]] = j;
        }
        int[] partner = new int[n];
        foreach (var p in pairs) {
            partner[p[0]] = p[1];
            partner[p[1]] = p[0];
        }
        int unhappy = 0;
        for (int x = 0; x < n; x++) {
            int y = partner[x];
            bool isUnhappy = false;
            for (int i = 0; i < rank[x][y]; i++) {
                int u = preferences[x][i];
                if (rank[u][x] < rank[u][partner[u]]) { isUnhappy = true; break; }
            }
            if (isUnhappy) unhappy++;
        }
        return unhappy;
    }
}
