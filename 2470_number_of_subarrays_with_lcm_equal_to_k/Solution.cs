// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

public class Solution {
    public int SubarrayLCM(int[] nums, int k) {
        int ans = 0, n = nums.Length;
        for (int i = 0; i < n; i++) {
            long cur = 1;
            for (int j = i; j < n; j++) {
                cur = cur / Gcd((int)cur, nums[j]) * nums[j];
                if (cur > k) break;
                if (cur == k) ans++;
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
