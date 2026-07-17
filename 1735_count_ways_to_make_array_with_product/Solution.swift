// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

class Solution {
    private let mod = 1_000_000_007

    func waysToFillArray(_ queries: [[Int]]) -> [Int] {
        var ans: [Int] = []
        ans.reserveCapacity(queries.count)
        for query in queries {
            let n = query[0]
            var value = query[1]
            var ways = 1
            var d = 2
            while d * d <= value {
                if value % d == 0 {
                    var exp = 0
                    while value % d == 0 {
                        value /= d
                        exp += 1
                    }
                    ways = ways * combMod(n + exp - 1, exp) % mod
                }
                d += d == 2 ? 1 : 2
            }
            if value > 1 {
                ways = ways * (n % mod) % mod
            }
            ans.append(ways)
        }
        return ans
    }

    private func combMod(_ a: Int, _ b: Int) -> Int {
        var num = 1
        var den = 1
        for i in stride(from: 1, through: b, by: 1) {
            num = num * ((a - b + i) % mod) % mod
            den = den * (i % mod) % mod
        }
        return num * powMod(den, mod - 2) % mod
    }

    private func powMod(_ base: Int, _ exp: Int) -> Int {
        var result = 1
        var b = base % mod
        var e = exp
        while e > 0 {
            if e & 1 == 1 {
                result = result * b % mod
            }
            b = b * b % mod
            e >>= 1
        }
        return result
    }
}
