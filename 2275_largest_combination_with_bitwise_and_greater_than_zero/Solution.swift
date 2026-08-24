// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution {
    func largestCombination(_ candidates: [Int]) -> Int {
        var ans = 0
        for bit in 0..<24 {
            var cnt = 0
            for x in candidates where ((x >> bit) & 1) != 0 { cnt += 1 }
            ans = max(ans, cnt)
        }
        return ans
    }
}
