// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution {
    func lengthAfterTransformations(_ s: String, _ t: Int, _ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var mat = Array(repeating: Array(repeating: 0, count: 26), count: 26)
        for i in 0..<26 {
            if nums[i] >= 1 {
                for j in 1...nums[i] { mat[i][(i + j) % 26] = 1 }
            }
        }
        mat = matPow(mat, t, mod)
        var cnt = Array(repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        var ans = 0
        for i in 0..<26 {
            for j in 0..<26 {
                ans = (ans + cnt[i] * mat[i][j] % mod) % mod
            }
        }
        return ans
    }

    private func matMul(_ a: [[Int]], _ b: [[Int]], _ mod: Int) -> [[Int]] {
        let n = a.count
        var c = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for k in 0..<n {
                if a[i][k] == 0 { continue }
                for j in 0..<n {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod
                }
            }
        }
        return c
    }

    private func matPow(_ a: [[Int]], _ e: Int, _ mod: Int) -> [[Int]] {
        let n = a.count
        var r = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n { r[i][i] = 1 }
        var a = a, e = e
        while e > 0 {
            if e & 1 != 0 { r = matMul(r, a, mod) }
            a = matMul(a, a, mod)
            e >>= 1
        }
        return r
    }
}
