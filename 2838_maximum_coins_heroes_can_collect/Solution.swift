// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

class Solution {
    func maximumCoins(_ heroes: [Int], _ monsters: [Int], _ coins: [Int]) -> [Int] {
        let n = monsters.count
        var idx = Array(0..<n)
        idx.sort { monsters[$0] < monsters[$1] }
        var pref = Array(repeating: 0, count: n + 1)
        var ms = Array(repeating: 0, count: n)
        for i in 0..<n {
            ms[i] = monsters[idx[i]]
            pref[i + 1] = pref[i] + coins[idx[i]]
        }
        var ans = Array(repeating: 0, count: heroes.count)
        for i in 0..<heroes.count {
            ans[i] = pref[upperBound(ms, heroes[i])]
        }
        return ans
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
