// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

class Solution {
    func countNonDecreasingArrays(_ digitSum: [Int]) -> Int {
        let mod = 1_000_000_007
        var groups = [[Int]](repeating: [], count: 51)
        for x in 0...5000 {
            var s = 0, y = x
            while y > 0 { s += y % 10; y /= 10 }
            groups[s].append(x)
        }
        var prevVals = groups[digitSum[0]]
        var dp = [Int](repeating: 1, count: prevVals.count)
        if digitSum.count > 1 {
            for pos in 1..<digitSum.count {
                let curVals = groups[digitSum[pos]]
                var next = [Int](repeating: 0, count: curVals.count)
                var j = 0, prefix = 0
                for i in 0..<curVals.count {
                    let x = curVals[i]
                    while j < prevVals.count && prevVals[j] <= x {
                        prefix += dp[j]
                        if prefix >= mod { prefix -= mod }
                        j += 1
                    }
                    next[i] = prefix
                }
                prevVals = curVals
                dp = next
            }
        }
        var ans = 0
        for x in dp {
            ans += x
            if ans >= mod { ans -= mod }
        }
        return ans
    }
}
