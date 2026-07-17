// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

class Solution {
    func getMaximumConsecutive(_ coins: [Int]) -> Int {
        var reach = 0
        for coin in coins.sorted() {
            if coin > reach + 1 { break }
            reach += coin
        }
        return reach + 1
    }
}
