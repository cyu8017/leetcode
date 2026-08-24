// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

class Solution {
    func numberOfWays(_ n: Int, _ limit: [Int]) -> Int {
        let MOD = 1_000_000_007
        let limit = limit.sorted()
        var points = [1, n]
        for x in limit {
            if x + 1 > 1 && x + 1 < n { points.append(x + 1) }
            if n - x > 1 && n - x < n { points.append(n - x) }
        }
        points.sort()
        var u = 0
        for i in 0..<points.count {
            if u == 0 || points[i] != points[u - 1] {
                points[u] = points[i]
                u += 1
            }
        }
        points = Array(points.prefix(u))
        var ans = 0
        if points.count >= 2 {
            for i in 0..<(points.count - 1) {
                let x = points[i]
                let a = countGE(limit, x), b = countGE(limit, n - x)
                let same = countGE(limit, max(x, n - x))
                var ways = (a * b - same) % MOD
                let length = points[i + 1] - x
                ans = (ans + ways * length) % MOD
            }
        }
        if ans < 0 { ans += MOD }
        return ans
    }

    private func countGE(_ limit: [Int], _ x: Int) -> Int {
        var lo = 0, hi = limit.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if limit[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return limit.count - lo
    }
}
