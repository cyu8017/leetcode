// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution {
    func maxDifference(_ s: String) -> Int {
        var freq = Array(repeating: 0, count: 26)
        for c in s { freq[Int(c.asciiValue! - 97)] += 1 }
        var maxOdd = 0, minEven = 1_000_000_000
        for f in freq {
            if f == 0 { continue }
            if f % 2 == 1 {
                if f > maxOdd { maxOdd = f }
            } else if f < minEven { minEven = f }
        }
        return maxOdd - minEven
    }
}
