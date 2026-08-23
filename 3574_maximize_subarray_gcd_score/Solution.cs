// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

using System;

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
    public long MaxGCDScore(int[] nums, int k) {
        int n = nums.Length;
        int[] cnt = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x % 2 == 0) { cnt[i]++; x /= 2; }
        }
        long ans = 0;
        for (int l = 0; l < n; l++) {
            int g = 0, mi = int.MaxValue, t = 0;
            for (int r = l; r < n; r++) {
                g = Gcd(g, nums[r]);
                if (cnt[r] < mi) { mi = cnt[r]; t = 1; }
                else if (cnt[r] == mi) t++;
                long score = 1L * g * (r - l + 1);
                if (t <= k) score *= 2;
                ans = Math.Max(ans, score);
            }
        }
        return ans;
    }
}
