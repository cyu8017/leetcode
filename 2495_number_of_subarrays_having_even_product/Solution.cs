// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

public class Solution {
    public long EvenProduct(int[] nums) {
        long n = nums.Length;
        long total = n * (n + 1) / 2;
        long oddLen = 0, odd = 0;
        foreach (int x in nums) {
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
