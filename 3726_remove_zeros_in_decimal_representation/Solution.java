// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution {
    public long removeZeros(long n) {
        long ans = 0, k = 1;
        while (n > 0) {
            long x = n % 10;
            if (x > 0) {
                ans = k * x + ans;
                k *= 10;
            }
            n /= 10;
        }
        return ans;
    }
}
