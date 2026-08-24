// CONFIG class=Solution method=minOperations types=None
// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

class Solution {
    public long minOperations(int[] nums, int k) {
        long[] evenFreq = new long[k], oddFreq = new long[k];
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) evenFreq[nums[i] % k]++;
            else oddFreq[nums[i] % k]++;
        }
        long[] evenCost = costs(evenFreq, k);
        long[] oddCost = costs(oddFreq, k);
        long best1 = 1L << 62, best2 = 1L << 62;
        int bestIndex = -1;
        for (int i = 0; i < k; i++) {
            long x = oddCost[i];
            if (x < best1) {
                best2 = best1;
                best1 = x;
                bestIndex = i;
            } else if (x < best2) best2 = x;
        }
        long ans = 1L << 62;
        for (int x = 0; x < k; x++) {
            long other = (x == bestIndex) ? best2 : best1;
            ans = Math.min(ans, evenCost[x] + other);
        }
        return ans;
    }

    private long[] costs(long[] freq, int k) {
        long[] dbl = new long[2 * k];
        for (int i = 0; i < 2 * k; i++) dbl[i] = freq[i % k];
        long[] countPrefix = new long[2 * k + 1], weightedPrefix = new long[2 * k + 1];
        for (int i = 0; i < 2 * k; i++) {
            countPrefix[i + 1] = countPrefix[i] + dbl[i];
            weightedPrefix[i + 1] = weightedPrefix[i] + (long) i * dbl[i];
        }
        long[] res = new long[k];
        int cw = k / 2, cc = (k - 1) / 2;
        for (int t = 0; t < k; t++) {
            long cnt = countPrefix[t + cw + 1] - countPrefix[t];
            long sum = weightedPrefix[t + cw + 1] - weightedPrefix[t];
            res[t] += sum - (long) t * cnt;
            if (cc > 0) {
                long cnt2 = countPrefix[t + k] - countPrefix[t + k - cc];
                long sum2 = weightedPrefix[t + k] - weightedPrefix[t + k - cc];
                res[t] += (long) (t + k) * cnt2 - sum2;
            }
        }
        return res;
    }
}
