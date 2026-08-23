// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

class Solution {
    public long maximizeXorAndXor(int[] nums) {
        int n = nums.length;
        long best = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int andVal = -1, xorRest = 0;
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) != 0) {
                    andVal = andVal < 0 ? nums[i] : (andVal & nums[i]);
                } else {
                    xorRest ^= nums[i];
                }
            }
            if (andVal < 0) andVal = 0;
            int comp = ((1 << n) - 1) ^ mask;
            for (int sub = comp; ; sub = (sub - 1) & comp) {
                int x1 = 0;
                for (int i = 0; i < n; i++)
                    if (((sub >> i) & 1) != 0) x1 ^= nums[i];
                int x2 = xorRest ^ x1;
                best = Math.max(best, (long)andVal + x1 + x2);
                if (sub == 0) break;
            }
        }
        return best;
    }
}
