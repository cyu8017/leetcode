// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

import java.util.HashSet;
import java.util.Set;

class Solution {
    static int Cost(int x, int t) {
        if (x == t) return 0;
        if (x % t == 0 || t % x == 0) return 1;
        return 2;
    }

    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public int minOperations(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;
        int g = nums[0], mn = nums[0];
        for (int i = 1; i < n; i++) {
            g = Gcd(g, nums[i]);
            mn = Math.min(mn, nums[i]);
        }
        var cands = new HashSet<Integer>();
        for (int x : nums) cands.add(x);
        for (int d = 1; 1L * d * d <= mn; d++) {
            if (mn % d == 0) {
                cands.add(d);
                cands.add(mn / d);
            }
        }
        cands.add(g);
        int ans = Integer.MAX_VALUE;
        for (int t : cands) {
            int sum = 0;
            for (int x : nums) {
                sum += Cost(x, t);
                if (sum >= ans) break;
            }
            ans = Math.min(ans, sum);
        }
        return ans;
    }
}
