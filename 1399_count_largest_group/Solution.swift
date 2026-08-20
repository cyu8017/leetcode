// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

class Solution {
    func countLargestGroup(_ n: Int) -> Int {
        var c = [Int: Int]()
        for x in 1...n {
            var s = 0, v = x
            while v > 0 { s += v % 10; v /= 10 }
            c[s, default: 0] += 1
        }
        let m = c.values.max() ?? 0
        return c.values.filter { $0 == m }.count
    }
}
