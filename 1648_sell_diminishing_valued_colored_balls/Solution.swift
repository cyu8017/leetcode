// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution {
    func maxProfit(_ inventory: [Int], _ orders: Int) -> Int {
        let MOD = 1_000_000_007
        var inv = inventory.sorted(by: >)
        inv.append(0)
        var orders = orders
        var ans = 0
        for i in 0..<(inv.count - 1) {
            let width = i + 1
            let high = inv[i], low = inv[i + 1]
            let balls = width * (high - low)
            let take = min(orders, balls)
            let full = take / width
            let rem = take % width
            let bottom = high - full
            // width * full * (high + bottom + 1) / 2 + rem * bottom
            var a = width, b = full, c = high + bottom + 1
            if a % 2 == 0 { a /= 2 }
            else if b % 2 == 0 { b /= 2 }
            else { c /= 2 }
            ans = (ans + mulMod(mulMod(a % MOD, b % MOD, MOD), c % MOD, MOD)) % MOD
            ans = (ans + mulMod(rem % MOD, bottom % MOD, MOD)) % MOD
            orders -= take
            if orders == 0 { break }
        }
        return ans
    }

    private func mulMod(_ a: Int, _ b: Int, _ MOD: Int) -> Int {
        Int((Int64(a) * Int64(b)) % Int64(MOD))
    }
}
