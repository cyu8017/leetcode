// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    private static class Hashing {
        long[] p, h;
        long mod;

        Hashing(String word, long bas, long mod) {
            this.mod = mod;
            int n = word.length();
            p = new long[n + 1];
            h = new long[n + 1];
            p[0] = 1;
            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * bas % mod;
                h[i] = (h[i - 1] * bas + word.charAt(i - 1)) % mod;
            }
        }

        long query(int l, int r) {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        }
    }

    public int minimumCost(String target, String[] words, int[] costs) {
        final long bas = 13331, mod = 998244353;
        final int inf = Integer.MAX_VALUE / 2;
        int n = target.length();
        Hashing hashing = new Hashing(target, bas, mod);
        int[] f = new int[n + 1];
        Arrays.fill(f, inf);
        f[0] = 0;
        Set<Integer> ss = new HashSet<>();
        for (String w : words) ss.add(w.length());
        List<Integer> lengths = new ArrayList<>(ss);
        lengths.sort(null);
        Map<Long, Integer> d = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            long x = 0;
            for (char c : words[i].toCharArray()) x = (x * bas + c) % mod;
            if (!d.containsKey(x) || costs[i] < d.get(x)) d.put(x, costs[i]);
        }
        for (int i = 1; i <= n; i++) {
            for (int j : lengths) {
                if (j > i) break;
                long x = hashing.query(i - j + 1, i);
                if (d.containsKey(x)) f[i] = Math.min(f[i], f[i - j] + d.get(x));
            }
        }
        return f[n] >= inf ? -1 : f[n];
    }
}
