// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution {
    func fillCups(_ amount: [Int]) -> Int {
        let a = amount.sorted()
        if a[2] >= a[0] + a[1] { return a[2] }
        return (a[0] + a[1] + a[2] + 1) / 2
    }
}
