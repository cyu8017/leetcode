// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

class Solution {
    func maxValue(_ n: Int, _ restrictions: [[Int]], _ diff: [Int]) -> Int {
        let INF = Int.max / 4
        var bound = [Int](repeating: INF, count: n)
        bound[0] = 0
        for r in restrictions { bound[r[0]] = r[1] }
        if n > 1 {
            for i in 1..<n { bound[i] = min(bound[i], bound[i - 1] + diff[i - 1]) }
            for i in stride(from: n - 2, through: 0, by: -1) {
                bound[i] = min(bound[i], bound[i + 1] + diff[i])
            }
        }
        var ans = bound[0]
        if n > 1 {
            for i in 1..<n { ans = max(ans, bound[i]) }
        }
        return ans
    }
}
