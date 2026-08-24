// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

class Solution {
    func getGoodIndices(_ variables: [[Int]], _ target: Int) -> [Int] {
        var ans: [Int] = []
        for i in 0..<variables.count {
            let v = variables[i]
            let a = v[0], b = v[1], c = v[2], m = v[3]
            if modPow(modPow(a, b, 10), c, m) == target { ans.append(i) }
        }
        return ans
    }

    private func modPow(_ a0: Int, _ b0: Int, _ mod: Int) -> Int {
        var res = 1 % mod
        var a = a0 % mod, b = b0
        while b > 0 {
            if b & 1 != 0 { res = res * a % mod }
            a = a * a % mod
            b >>= 1
        }
        return res
    }
}
