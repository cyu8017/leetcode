// LeetCode 1716 - Calculate Money in Leetcode Bank
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int days = n % 7;
        return weeks * 28 + 7 * weeks * (weeks - 1) / 2 + days * (weeks + 1) + days * (days - 1) / 2;
    }
}
