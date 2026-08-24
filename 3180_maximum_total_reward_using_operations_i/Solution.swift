// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

class Solution {
    private var rewardValues: [Int] = []
    private var f: [Int] = []
    private var n = 0

    func maxTotalReward(_ rewardValues: [Int]) -> Int {
        let rv = rewardValues.sorted()
        self.rewardValues = rv
        n = rv.count
        f = Array(repeating: -1, count: rv[n - 1] << 1)
        return dfs(0)
    }

    private func dfs(_ x: Int) -> Int {
        if f[x] != -1 { return f[x] }
        let idx = upperBound(rewardValues, x)
        f[x] = 0
        for it in idx..<n {
            f[x] = max(f[x], rewardValues[it] + dfs(x + rewardValues[it]))
        }
        return f[x]
    }

    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
