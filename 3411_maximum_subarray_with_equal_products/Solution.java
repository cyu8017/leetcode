// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

class Solution {
    private static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int maxLength(int[] nums) {
        int n = nums.length;
        int ans = 1;
        for (int i = 0; i < n; i++) {
            long prod = 1;
            int g = 0, l = 1;
            for (int j = i; j < n; j++) {
                if (prod > 1_000_000_000L / nums[j]) break;
                prod *= nums[j];
                if (g == 0) {
                    g = nums[j];
                    l = nums[j];
                } else {
                    g = gcd(g, nums[j]);
                    l = l / gcd(l, nums[j]) * nums[j];
                }
                if (prod == (long) l * g && j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
}
