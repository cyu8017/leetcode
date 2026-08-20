// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

class Solution {
    func maximumNumberOfOnes(_ width: Int, _ height: Int, _ sideLength: Int, _ maxOnes: Int) -> Int {
        var counts: [Int] = []
        for r in 0..<sideLength {
            for c in 0..<sideLength {
                let rows = (height - r + sideLength - 1) / sideLength
                let cols = (width - c + sideLength - 1) / sideLength
                counts.append(rows * cols)
            }
        }
        counts.sort(by: >)
        var ans = 0
        for i in 0..<min(maxOnes, counts.count) { ans += counts[i] }
        return ans
    }
}
