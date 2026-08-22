// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

int minimumPossibleSum(int n, int target) {
    const int mod = 1000000007;
    long long m = target / 2;
    if (n <= m) {
        return (int)((long long)n * (n + 1) / 2 % mod);
    }
    long long sum = m * (m + 1) / 2;
    long long remain = n - m;
    sum += remain * target + remain * (remain - 1) / 2;
    return (int)(sum % mod);
}
