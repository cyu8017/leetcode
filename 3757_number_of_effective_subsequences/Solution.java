// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

import java.util.ArrayList;
import java.util.List;

class Solution {
    static int PopCount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public int countEffectiveSubsequences(int[] nums) {
        final int mod = 1000000007;
        int all = 0;
        for (int x : nums) all |= x;
        var bits = new ArrayList<Integer>();
        for (int b = 0; b < 20; b++) if (((all >> b) & 1) != 0) bits.add(b);
        int m = bits.size();
        int[] freq = new int[1 << m];
        for (int x : nums) {
            int mask = 0;
            for (int i = 0; i < m; i++) if (((x >> bits.get(i)) & 1) != 0) mask |= 1 << i;
            freq[mask]++;
        }
        int[] disjoint = freq.clone();
        for (int b = 0; b < m; b++) {
            for (int mask = 0; mask < (1 << m); mask++) {
                if (((mask >> b) & 1) != 0) disjoint[mask] += disjoint[mask ^ (1 << b)];
            }
        }
        int[] pow2 = new int[nums.length + 1];
        pow2[0] = 1;
        for (int i = 1; i <= nums.length; i++) pow2[i] = pow2[i - 1] * 2 % mod;
        int ans = 0, full = (1 << m) - 1;
        for (int s = 1; s <= full; s++) {
            int ways = pow2[disjoint[full ^ s]];
            int bc = PopCount(s);
            if ((bc & 1) != 0) {
                ans += ways;
                if (ans >= mod) ans -= mod;
            } else {
                ans -= ways;
                if (ans < 0) ans += mod;
            }
        }
        return ans;
    }
}
