// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

class Solution {
    func shoppingOffers(_ price: [Int], _ special: [[Int]], _ needs: [Int]) -> Int {
        var memo = [[Int]: Int]()
        func dfs(_ state: [Int]) -> Int {
            if let cached = memo[state] { return cached }
            var cost = 0
            for i in 0..<price.count { cost += state[i] * price[i] }
            for offer in special {
                var nxt = state
                var valid = true
                for i in 0..<price.count {
                    if nxt[i] < offer[i] { valid = false; break }
                    nxt[i] -= offer[i]
                }
                if valid {
                    cost = min(cost, offer[price.count] + dfs(nxt))
                }
            }
            memo[state] = cost
            return cost
        }
        return dfs(needs)
    }
}
