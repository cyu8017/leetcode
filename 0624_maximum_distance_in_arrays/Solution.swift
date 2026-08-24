// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution {
    func maxDistance(_ arrays: [[Int]]) -> Int {
        var minVal = arrays[0][0]
        var maxVal = arrays[0].last!
        var best = 0
        for i in 1..<arrays.count {
            let first = arrays[i][0]
            let last = arrays[i].last!
            best = max(best, max(abs(last - minVal), abs(maxVal - first)))
            minVal = min(minVal, first)
            maxVal = max(maxVal, last)
        }
        return best
    }
}
