// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution {
    func maxRunTime(_ n: Int, _ batteries: [Int]) -> Int {
        let sum = batteries.reduce(0, +)
        var lo = 1, hi = sum / n
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            let need = batteries.reduce(0) { $0 + min($1, mid) }
            if need >= mid * n { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }
}
