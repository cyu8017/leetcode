// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution {
    func trimMean(_ arr: [Int]) -> Double {
        let sorted = arr.sorted()
        let k = sorted.count / 20
        let sliced = sorted[k..<(sorted.count - k)]
        return Double(sliced.reduce(0, +)) / Double(sliced.count)
    }
}
