// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

class Solution {
    func xorAfterQueries(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        var byK = [Int: [[Int]]]()
        for q in queries { byK[q[2], default: []].append(q) }
        var res = nums
        for (_, qs) in byK {
            var fac = Array(repeating: 1, count: n)
            for u in qs {
                var i = u[0]
                while i <= u[1] {
                    fac[i] = fac[i] * u[3] % MOD
                    i += u[2]
                }
            }
            for i in 0..<n { res[i] = res[i] * fac[i] % MOD }
        }
        var ans = 0
        for v in res { ans ^= v }
        return ans
    }
}
