// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

class Solution {
    func minArrivalsToDiscard(_ arrivals: [Int], _ w: Int, _ m: Int) -> Int {
        var cnt = [Int: Int]()
        let n = arrivals.count
        var marked = Array(repeating: 0, count: n)
        var ans = 0
        for i in 0..<n {
            let x = arrivals[i]
            if i >= w { cnt[arrivals[i - w], default: 0] -= marked[i - w] }
            if (cnt[x] ?? 0) >= m { ans += 1 }
            else {
                marked[i] = 1
                cnt[x, default: 0] += 1
            }
        }
        return ans
    }
}
