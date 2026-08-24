// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

class Solution {
    func distanceSum(_ m: Int, _ n: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        if k < 2 { return 0 }
        let totalCells = m * n
        let pairChoose = comb(totalCells - 2, k - 2, mod)
        var sumDist = 0
        if m > 1 {
            for d in 1..<m { sumDist += d * (m - d) * n * n }
        }
        if n > 1 {
            for d in 1..<n { sumDist += d * (n - d) * m * m }
        }
        return sumDist % mod * pairChoose % mod
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = a % mod, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }

    private func comb(_ n: Int, _ k: Int, _ mod: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var num = 1, den = 1
        if k > 0 {
            for i in 0..<k {
                num = num * (n - i) % mod
                den = den * (i + 1) % mod
            }
        }
        return num * modPow(den, mod - 2, mod) % mod
    }
}
