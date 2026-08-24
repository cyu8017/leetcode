// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

class Solution {
    func countTrapezoids(_ points: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var cnt = [Int: Int]()
        for p in points { cnt[p[1], default: 0] += 1 }
        var ans = 0, pre = 0
        for c in cnt.values {
            let lines = c * (c - 1) / 2
            ans = (ans + pre * lines) % MOD
            pre = (pre + lines) % MOD
        }
        return ans
    }
}
