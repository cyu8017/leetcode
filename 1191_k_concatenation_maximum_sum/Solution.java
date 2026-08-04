// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        final int MOD = 1_000_000_007;
        long one = kadane(arr);
        if (k == 1) return (int) (one % MOD);
        int[] twice = new int[arr.length * 2];
        System.arraycopy(arr, 0, twice, 0, arr.length);
        System.arraycopy(arr, 0, twice, arr.length, arr.length);
        long two = kadane(twice);
        long total = 0;
        for (int x : arr) total += x;
        long ans;
        if (total > 0) ans = Math.max(one, two + total * (k - 2));
        else ans = Math.max(one, two);
        return (int) (ans % MOD);
    }
    private long kadane(int[] nums) {
        long best = 0, cur = 0;
        for (int x : nums) {
            cur = Math.max(0, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    }
}
