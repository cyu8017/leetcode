// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution {
    func minimizedMaximum(_ n: Int, _ quantities: [Int]) -> Int {
        var lo = 1, hi = quantities.max() ?? 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if can(n, quantities, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func can(_ n: Int, _ quantities: [Int], _ x: Int) -> Bool {
        var need = 0
        for q in quantities {
            need += (q + x - 1) / x
            if need > n { return false }
        }
        return true
    }
}
