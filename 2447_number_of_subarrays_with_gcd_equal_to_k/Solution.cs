// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

public class Solution {
    public int SubarrayGCD(int[] nums, int k) {
        int ans = 0, n = nums.Length;
        for (int i = 0; i < n; i++) {
            int g = 0;
            for (int j = i; j < n; j++) {
                g = Gcd(g, nums[j]);
                if (g < k) break;
                if (g == k) ans++;
            }
        }
        return ans;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
