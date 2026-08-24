// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

class Solution {
    private let mod = 1_000_000_007

    func numberOfWays(_ s: String, _ t: String, _ k: Int) -> Int {
        let n = s.count
        let ss = s + s
        let ssArr = Array(ss)
        let tArr = Array(t)
        var found = false
        for i in 0..<(2 * n - 1) {
            if Array(ssArr[i..<(i + n)]) == tArr {
                found = true
                break
            }
        }
        if !found { return 0 }
        var cnt = 0
        for i in 0..<n {
            if Array(ssArr[i..<(i + n)]) == tArr { cnt += 1 }
        }
        let same = s == t
        let pk = modPow(n - 1, k)
        let invn = modPow(n, mod - 2)
        let sign = (k % 2 == 1) ? mod - 1 : 1
        let waysSame = (pk + ((n - 1) % mod) * sign % mod) % mod * invn % mod
        let waysDiff = (pk - sign + mod) % mod * invn % mod
        if same { return waysSame }
        return waysDiff * cnt % mod
    }

    private func modPow(_ a0: Int, _ b0: Int) -> Int {
        var a = a0 % mod, b = b0, res = 1
        while b > 0 {
            if b & 1 != 0 { res = res * a % mod }
            a = a * a % mod
            b >>= 1
        }
        return res
    }
}
