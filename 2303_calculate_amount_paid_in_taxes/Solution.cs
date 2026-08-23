// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

public class Solution {
    public double CalculateTax(int[][] brackets, int income) {
        double ans = 0;
        int prev = 0;
        foreach (var b in brackets) {
            int upper = b[0], percent = b[1];
            if (income <= prev) break;
            int taxable = (income < upper) ? income - prev : upper - prev;
            ans += taxable * percent / 100.0;
            prev = upper;
        }
        return ans;
    }
}
