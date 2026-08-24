// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution {

    fun calculateTax(brackets: Array<IntArray>, income: Int): Double {

            var ans = 0
            var prev = 0
            for (b in brackets) {
                var upper = b[0]; var percent = b[1]
                if (income <= prev) break
                var taxable = if ((income < upper)) income - prev else upper - prev
                ans += taxable * percent / 100.0
                prev = upper
            }
            return ans

    }

}
