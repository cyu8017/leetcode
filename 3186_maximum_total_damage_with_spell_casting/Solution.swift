// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution {
    private var power: [Int] = []
    private var nxt: [Int] = []
    private var f: [Int] = []
    private var cnt: [Int: Int] = [:]
    private var n = 0

    func maximumTotalDamage(_ power: [Int]) -> Int {
        let p = power.sorted()
        n = p.count
        self.power = p
        cnt = [:]
        nxt = Array(repeating: 0, count: n)
        f = Array(repeating: -1, count: n)
        for i in 0..<n {
            cnt[p[i], default: 0] += 1
            nxt[i] = lowerBound(p, p[i] + 3)
        }
        return dfs(0)
    }

    private func dfs(_ i: Int) -> Int {
        if i >= n { return 0 }
        if f[i] != -1 { return f[i] }
        let a = dfs(i + cnt[power[i]]!)
        let b = power[i] * cnt[power[i]]! + dfs(nxt[i])
        f[i] = max(a, b)
        return f[i]
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
