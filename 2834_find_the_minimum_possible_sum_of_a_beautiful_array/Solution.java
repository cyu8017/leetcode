// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution {
    public int minimumPossibleSum(int n, int target) {
        final int MOD = 1000000007;
        int m = target / 2;
        if (n <= m) return (int) (1L * n * (n + 1) / 2 % MOD);
        long sum = 1L * m * (m + 1) / 2;
        int remain = n - m;
        sum += 1L * remain * target + 1L * remain * (remain - 1) / 2;
        return (int) (sum % MOD);
    }
}
