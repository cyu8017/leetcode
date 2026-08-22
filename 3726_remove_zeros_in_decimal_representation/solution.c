// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

long long removeZeros(long long n) {
    long long ans = 0, k = 1;
    while (n > 0) {
        long long x = n % 10;
        if (x > 0) { ans = k * x + ans; k *= 10; }
        n /= 10;
    }
    return ans;
}
