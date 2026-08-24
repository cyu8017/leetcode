// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution {
    func minimumAverage(_ nums: [Int]) -> Double {
        let a = nums.sorted()
        let n = a.count
        var ans = 1 << 30
        for i in 0..<(n / 2) { ans = min(ans, a[i] + a[n - i - 1]) }
        return Double(ans) / 2.0
    }
}
