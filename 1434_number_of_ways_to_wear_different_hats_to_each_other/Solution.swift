// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

class Solution {
    func numberWays(_ hats: [[Int]]) -> Int {
        let mod = 1_000_000_007, people = hats.count
        var wearers = Array(repeating: [Int](), count: 41)
        for (person, choices) in hats.enumerated() {
            for hat in choices { wearers[hat].append(person) }
        }
        var dp = Array(repeating: 0, count: 1 << people)
        dp[0] = 1
        for hat in 1...40 {
            var nxt = dp
            for mask in 0..<dp.count {
                let ways = dp[mask]
                if ways == 0 { continue }
                for person in wearers[hat] where mask & (1 << person) == 0 {
                    nxt[mask | (1 << person)] = (nxt[mask | (1 << person)] + ways) % mod
                }
            }
            dp = nxt
        }
        return dp[(1 << people) - 1]
    }
}
