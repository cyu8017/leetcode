// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

import java.util.HashMap;
import java.util.Map;

class Solution {
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= n / i; i++)
            if (n % i == 0) return false;
        return true;
    }

    public int mostFrequentPrime(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int a = -1; a <= 1; a++) {
                    for (int b = -1; b <= 1; b++) {
                        if (a == 0 && b == 0) continue;
                        int x = i + a, y = j + b, v = mat[i][j];
                        while (x >= 0 && x < m && y >= 0 && y < n) {
                            v = v * 10 + mat[x][y];
                            if (isPrime(v)) {
                                cnt.put(v, cnt.getOrDefault(v, 0) + 1);
                            }
                            x += a;
                            y += b;
                        }
                    }
                }
            }
        }
        int ans = -1, mx = 0;
        for (Map.Entry<Integer, Integer> kv : cnt.entrySet()) {
            if (mx < kv.getValue() || (mx == kv.getValue() && ans < kv.getKey())) {
                mx = kv.getValue();
                ans = kv.getKey();
            }
        }
        return ans;
    }
}
