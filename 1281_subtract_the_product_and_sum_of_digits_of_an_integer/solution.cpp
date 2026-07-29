// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1, total = 0;
        while (n) {
            int digit = n % 10;
            n /= 10;
            product *= digit;
            total += digit;
        }
        return product - total;
    }
};
