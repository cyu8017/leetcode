// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

using System;

public class Solution {
    public long MinOperations(int[] nums, int k) {
        long[] evenFreq = new long[k], oddFreq = new long[k];
        for (int i = 0; i < nums.Length; i++) {
            if (i % 2 == 0) evenFreq[nums[i] % k]++;
            else oddFreq[nums[i] % k]++;
        }
        long[] Costs(long[] freq) {
            long[] dbl = new long[2 * k];
            for (int i = 0; i < 2 * k; i++) dbl[i] = freq[i % k];
            long[] countPrefix = new long[2 * k + 1], weightedPrefix = new long[2 * k + 1];
            for (int i = 0; i < 2 * k; i++) {
                countPrefix[i + 1] = countPrefix[i] + dbl[i];
                weightedPrefix[i + 1] = weightedPrefix[i] + (long)i * dbl[i];
            }
            (long cnt, long sum) RangeStats(int l, int r) {
                return (countPrefix[r + 1] - countPrefix[l], weightedPrefix[r + 1] - weightedPrefix[l]);
            }
            long[] res = new long[k];
            int cw = k / 2, cc = (k - 1) / 2;
            for (int t = 0; t < k; t++) {
                var (cnt, sum) = RangeStats(t, t + cw);
                res[t] += sum - (long)t * cnt;
                if (cc > 0) {
                    var (cnt2, sum2) = RangeStats(t + k - cc, t + k - 1);
                    res[t] += (long)(t + k) * cnt2 - sum2;
                }
            }
            return res;
        }
        long[] evenCost = Costs(evenFreq);
        long[] oddCost = Costs(oddFreq);
        long best1 = 1L << 62, best2 = 1L << 62;
        int bestIndex = -1;
        for (int i = 0; i < k; i++) {
            long x = oddCost[i];
            if (x < best1) { best2 = best1; best1 = x; bestIndex = i; }
            else if (x < best2) best2 = x;
        }
        long ans = 1L << 62;
        for (int x = 0; x < k; x++) {
            long other = (x == bestIndex) ? best2 : best1;
            ans = Math.Min(ans, evenCost[x] + other);
        }
        return ans;
    }
}
