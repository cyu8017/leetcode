// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

import java.util.Arrays;

class Solution {
    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        int n = flowers.length;
        for (int i = 0; i < n; i++) if (flowers[i] > target) flowers[i] = target;
        Arrays.sort(flowers);
        long sum = 0;
        for (int f : flowers) sum += f;
        if ((long)target * n - sum <= newFlowers) return (long)n * full;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + flowers[i];
        long ans = 0;
        int j = n - 1;
        long remain = newFlowers;
        for (int complete = 0; complete <= n; complete++) {
            if (complete > 0) {
                long need = target - flowers[n - complete];
                if (remain < need) break;
                remain -= need;
            }
            while (j >= n - complete || (j >= 0 && (long)flowers[j] * (j + 1) - pref[j + 1] > remain)) j--;
            long partialVal = 0;
            if (j >= 0) {
                long extra = (remain - ((long)flowers[j] * (j + 1) - pref[j + 1])) / (j + 1);
                partialVal = flowers[j] + extra;
                if (partialVal >= target) partialVal = target - 1;
            }
            ans = Math.max(ans, (long)complete * full + partialVal * partial);
        }
        return ans;
    }
}
