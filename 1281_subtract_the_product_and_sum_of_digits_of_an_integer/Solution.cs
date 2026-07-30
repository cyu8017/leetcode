// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

public class Solution {
    public int SubtractProductAndSum(int n) {
        int product = 1, total = 0;
        while (n > 0) {
            int digit = n % 10;
            product *= digit;
            total += digit;
            n /= 10;
        }
        return product - total;
    }
}
