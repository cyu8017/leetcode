// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

class Solution {
    public long evenProduct(int[] nums) {
        long n = nums.length;
        long total = n * (n + 1) / 2;
        long oddLen = 0, odd = 0;
        for (int x : nums) {
            if (x % 2 == 1) {
                odd++;
                oddLen += odd;
            } else {
                odd = 0;
            }
        }
        return total - oddLen;
    }
}
