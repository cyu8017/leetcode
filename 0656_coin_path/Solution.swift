// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

class Solution {
    func cheapestJump(_ coins: [Int], _ maxJump: Int) -> [Int] {
        let n = coins.count
        if coins[n - 1] == -1 { return [] }
        let inf = Int.max / 4
        var cost = Array(repeating: inf, count: n)
        var nxt = Array(repeating: -1, count: n)
        cost[n - 1] = coins[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            if coins[i] == -1 { continue }
            for jump in 1...maxJump {
                let j = i + jump
                if j >= n { break }
                if cost[j] == inf { continue }
                let candidate = coins[i] + cost[j]
                if candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i])) {
                    cost[i] = candidate
                    nxt[i] = j
                }
            }
        }
        if cost[0] == inf { return [] }
        var path = [1]
        var i = 0
        while i != n - 1 {
            i = nxt[i]
            path.append(i + 1)
        }
        return path
    }
}
