// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

class Solution {
    private static let C: [[Int]] = {
        let MX = 50
        var c = Array(repeating: [Int](repeating: 0, count: MX + 1), count: MX)
        for i in 0..<MX {
            c[i][0] = 1
            if i >= 1 {
                for j in 1...i { c[i][j] = c[i - 1][j - 1] + c[i - 1][j] }
            }
        }
        return c
    }()

    func nthSmallest(_ n: Int, _ k: Int) -> Int {
        var n = n, k = k
        var ans = 0
        for i in stride(from: 49, through: 0, by: -1) {
            if n > Solution.C[i][k] {
                n -= Solution.C[i][k]
                ans |= 1 << i
                k -= 1
                if k == 0 { break }
            }
        }
        return ans
    }
}
