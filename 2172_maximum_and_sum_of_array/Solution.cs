// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

public class Solution {
    public int MaximumANDSum(int[] nums, int numSlots) {
        int n = nums.Length, slots = numSlots, maxMask = 1;
        for (int i = 0; i < slots; i++) maxMask *= 3;
        int[] dp = new int[maxMask];
        for (int mask = 0; mask < maxMask; mask++) {
            int cnt = 0, x = mask;
            while (x > 0) { cnt += x % 3; x /= 3; }
            if (cnt >= n) continue;
            int v = nums[cnt], bas = 1;
            for (int s = 1; s <= slots; s++) {
                int occ = (mask / bas) % 3;
                if (occ < 2) {
                    int nm = mask + bas;
                    dp[nm] = Math.Max(dp[nm], dp[mask] + (v & s));
                }
                bas *= 3;
            }
        }
        int best = 0;
        foreach (int v in dp) best = Math.Max(best, v);
        return best;
    }
}
