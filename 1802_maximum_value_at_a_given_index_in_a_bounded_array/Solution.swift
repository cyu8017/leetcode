// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution {
    func maxValue(_ n: Int, _ index: Int, _ maxSum: Int) -> Int {
        func minSideSum(_ value: Int, _ count: Int) -> Int {
            if value > count {
                return (value - 1 + value - count) * count / 2
            }
            return value * (value - 1) / 2 + (count - value + 1)
        }

        var lo = 1
        var hi = maxSum
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            let total = minSideSum(mid, index) + mid + minSideSum(mid, n - index - 1)
            if total <= maxSum {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return lo
    }
}
