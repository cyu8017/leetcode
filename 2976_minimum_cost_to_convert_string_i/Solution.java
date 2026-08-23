// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution {
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        final long inf = 1L << 60;
        long[][] dist = new long[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) dist[i][j] = inf;
            dist[i][i] = 0;
        }
        for (int i = 0; i < original.length; i++) {
            int u = original[i].charAt(0) - 'a';
            int v = changed[i].charAt(0) - 'a';
            long ww = cost[i];
            if (ww < dist[u][v]) dist[u][v] = ww;
        }
        for (int k = 0; k < 26; k++)
            for (int i = 0; i < 26; i++)
                for (int j = 0; j < 26; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        long ans = 0;
        for (int i = 0; i < source.length(); i++) {
            int a = source.charAt(i) - 'a', b = target.charAt(i) - 'a';
            if (dist[a][b] >= inf / 2) return -1;
            ans += dist[a][b];
        }
        return ans;
    }
}
