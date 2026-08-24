// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution {
    func calculateTax(_ brackets: [[Int]], _ income: Int) -> Double {
        var ans = 0.0, prev = 0
        for b in brackets {
            let upper = b[0], percent = b[1]
            if income <= prev { break }
            let taxable = income < upper ? income - prev : upper - prev
            ans += Double(taxable * percent) / 100.0
            prev = upper
        }
        return ans
    }
}
