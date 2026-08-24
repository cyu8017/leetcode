// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution {
    func goodDaysToRobBank(_ security: [Int], _ time: Int) -> [Int] {
        let n = security.count
        if time == 0 { return Array(0..<n) }
        var left = [Int](repeating: 0, count: n)
        var right = [Int](repeating: 0, count: n)
        for i in 1..<n where security[i] <= security[i - 1] { left[i] = left[i - 1] + 1 }
        for i in stride(from: n - 2, through: 0, by: -1) where security[i] <= security[i + 1] {
            right[i] = right[i + 1] + 1
        }
        return (time..<(n - time)).filter { left[$0] >= time && right[$0] >= time }
    }
}
