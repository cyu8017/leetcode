// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

public class Solution {
    public long MinimumCost(string source, string target, string[] original, string[] changed, int[] cost) {
        const long inf = 1L << 60;
        long[][] dist = new long[26][];
        for (int i = 0; i < 26; i++) {
            dist[i] = new long[26];
            for (int j = 0; j < 26; j++) dist[i][j] = inf;
            dist[i][i] = 0;
        }
        for (int i = 0; i < original.Length; i++) {
            int u = original[i][0] - 'a';
            int v = changed[i][0] - 'a';
            long ww = cost[i];
            if (ww < dist[u][v]) dist[u][v] = ww;
        }
        for (int k = 0; k < 26; k++)
            for (int i = 0; i < 26; i++)
                for (int j = 0; j < 26; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        long ans = 0;
        for (int i = 0; i < source.Length; i++) {
            int a = source[i] - 'a', b = target[i] - 'a';
            if (dist[a][b] >= inf / 2) return -1;
            ans += dist[a][b];
        }
        return ans;
    }
}
