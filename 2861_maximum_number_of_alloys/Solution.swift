// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

class Solution {
    func maxNumberOfAlloys(_ n: Int, _ k: Int, _ budget: Int, _ composition: [[Int]], _ stock: [Int], _ cost: [Int]) -> Int {
        var lo = 0, hi = 1_000_000_000, ans = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            if ok(mid, n, budget, composition, stock, cost) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    private func ok(_ machines: Int, _ n: Int, _ budget: Int, _ composition: [[Int]], _ stock: [Int], _ cost: [Int]) -> Bool {
        for comp in composition {
            var spend = 0
            for i in 0..<n {
                let need = machines * comp[i] - stock[i]
                if need > 0 { spend += need * cost[i] }
            }
            if spend <= budget { return true }
        }
        return false
    }
}
