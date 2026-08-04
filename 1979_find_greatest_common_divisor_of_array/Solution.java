// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution {
    public int findGCD(int[] nums) {
        int mn = nums[0], mx = nums[0];
        for (int x : nums) {
            mn = Math.min(mn, x);
            mx = Math.max(mx, x);
        }
        return gcd(mn, mx);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
