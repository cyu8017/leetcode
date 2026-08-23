// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length, ones = 0;
        for (int x : nums) if (x == 1) ones++;
        if (ones > 0) return n - ones;
        int best = n + 1;
        for (int i = 0; i < n; i++) {
            int g = 0;
            for (int j = i; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    best = Math.min(best, j - i);
                    break;
                }
            }
        }
        if (best == n + 1) return -1;
        return best + n - 1;
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
