// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

public class Solution {
    public int MaximumTotalValue(int[] value, int[] decay, long m) {
        const long mod = 1000000007;
        long CountAtLeast(long threshold) {
            long count = 0;
            for (int i = 0; i < value.Length; i++) {
                if (value[i] >= threshold) {
                    count += (value[i] - threshold) / decay[i] + 1;
                }
            }
            return count;
        }
        if (CountAtLeast(1) <= m) {
            long sum = 0;
            for (int i = 0; i < value.Length; i++) {
                long terms = (value[i] - 1L) / decay[i] + 1;
                sum = (sum + terms * value[i] - (long)decay[i] * terms * (terms - 1) / 2) % mod;
            }
            return (int)sum;
        }
        long high = 0;
        foreach (int v in value) if (v > high) high = v;
        long low = 1;
        while (low < high) {
            long mid = (low + high + 1) / 2;
            if (CountAtLeast(mid) >= m) low = mid;
            else high = mid - 1;
        }
        long threshold = low;
        long count = 0, sum2 = 0;
        for (int i = 0; i < value.Length; i++) {
            if (value[i] < threshold) continue;
            long terms = (value[i] - threshold) / decay[i] + 1;
            count += terms;
            sum2 = (sum2 + (terms * value[i] - (long)decay[i] * terms * (terms - 1) / 2) % mod) % mod;
        }
        sum2 = (sum2 - ((count - m) % mod) * (threshold % mod)) % mod;
        if (sum2 < 0) sum2 += mod;
        return (int)sum2;
    }
}
