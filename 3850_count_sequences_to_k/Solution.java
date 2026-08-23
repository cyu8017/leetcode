// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[] nums;
    private long k;
    private Map<String, Integer> f = new HashMap<>();

    public int countSequences(int[] nums, long k) {
        this.nums = nums;
        this.k = k;
        f.clear();
        return dfs(0, 1, 1);
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private int dfs(int i, long p, long q) {
        if (i == nums.length) return (p == k && q == 1) ? 1 : 0;
        String key = i + "," + p + "," + q;
        if (f.containsKey(key)) return f.get(key);
        int res = dfs(i + 1, p, q);
        long x = nums[i];
        long g1 = gcd(p * x, q);
        res += dfs(i + 1, (p * x) / g1, q / g1);
        long g2 = gcd(p, q * x);
        res += dfs(i + 1, p / g2, (q * x) / g2);
        f.put(key, res);
        return res;
    }
}
