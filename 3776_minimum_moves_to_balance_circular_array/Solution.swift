// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

class Solution {
    func minMoves(_ balance: [Int]) -> Int {
        var sum = 0
        for b in balance { sum += b }
        if sum < 0 { return -1 }

        let n = balance.count
        var mn = balance[0], idx = 0
        if n > 1 {
            for i in 1..<n {
                if balance[i] < mn {
                    mn = balance[i]
                    idx = i
                }
            }
        }
        if mn >= 0 { return 0 }

        var need = -mn
        var ans = 0
        if n > 1 {
            for j in 1..<n {
                let a = balance[(idx - j + n) % n]
                let b = balance[(idx + j) % n]
                let c1 = min(a, need)
                need -= c1
                ans += c1 * j
                let c2 = min(b, need)
                need -= c2
                ans += c2 * j
            }
        }
        return ans
    }
}
