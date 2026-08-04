// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
    public boolean isGoodArray(int[] nums) {
        int g = nums[0];
        for (int i = 1; i < nums.length; i++) g = gcd(g, nums[i]);
        return g == 1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }
}

