// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

using System.Collections.Generic;

public class Solution {
    static bool IsPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= n / i; i++)
            if (n % i == 0) return false;
        return true;
    }

    public int MostFrequentPrime(int[][] mat) {
        int m = mat.Length, n = mat[0].Length;
        var cnt = new Dictionary<int, int>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int a = -1; a <= 1; a++) {
                    for (int b = -1; b <= 1; b++) {
                        if (a == 0 && b == 0) continue;
                        int x = i + a, y = j + b, v = mat[i][j];
                        while (x >= 0 && x < m && y >= 0 && y < n) {
                            v = v * 10 + mat[x][y];
                            if (IsPrime(v)) {
                                cnt.TryGetValue(v, out int c);
                                cnt[v] = c + 1;
                            }
                            x += a;
                            y += b;
                        }
                    }
                }
            }
        }
        int ans = -1, mx = 0;
        foreach (var kv in cnt) {
            if (mx < kv.Value || (mx == kv.Value && ans < kv.Key)) {
                mx = kv.Value;
                ans = kv.Key;
            }
        }
        return ans;
    }
}
