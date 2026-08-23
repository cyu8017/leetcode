// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution {
    public long sumDigitDifferences(int[] nums) {
        int n = nums.length;
        int m = (int) Math.floor(Math.log10(nums[0])) + 1;
        long ans = 0;
        int[] vals = nums.clone();
        for (int k = 0; k < m; k++) {
            int[] cnt = new int[10];
            for (int i = 0; i < n; i++) {
                cnt[vals[i] % 10]++;
                vals[i] /= 10;
            }
            for (int v : cnt) ans += 1L * v * (n - v);
        }
        return ans / 2;
    }
}
