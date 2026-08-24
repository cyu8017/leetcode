// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

class Solution {
    func mostFrequentPrime(_ mat: [[Int]]) -> Int {
        let m = mat.count, n = mat[0].count
        var cnt: [Int: Int] = [:]
        for i in 0..<m {
            for j in 0..<n {
                for a in -1...1 {
                    for b in -1...1 {
                        if a == 0 && b == 0 { continue }
                        var x = i + a, y = j + b, v = mat[i][j]
                        while x >= 0 && x < m && y >= 0 && y < n {
                            v = v * 10 + mat[x][y]
                            if isPrime(v) { cnt[v, default: 0] += 1 }
                            x += a
                            y += b
                        }
                    }
                }
            }
        }
        var ans = -1, mx = 0
        for (k, v) in cnt {
            if mx < v || (mx == v && ans < k) {
                mx = v
                ans = k
            }
        }
        return ans
    }

    private func isPrime(_ n: Int) -> Bool {
        if n < 2 { return false }
        var i = 2
        while i <= n / i {
            if n % i == 0 { return false }
            i += 1
        }
        return true
    }
}
