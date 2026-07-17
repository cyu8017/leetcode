// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

class Solution {
    func closestCost(_ baseCosts: [Int], _ toppingCosts: [Int], _ target: Int) -> Int {
        var best = Int.max / 2

        func dfs(_ i: Int, _ cur: Int) {
            let curDiff = abs(cur - target)
            let bestDiff = abs(best - target)
            if curDiff < bestDiff || (curDiff == bestDiff && cur < best) {
                best = cur
            }
            if i == toppingCosts.count || cur >= target {
                return
            }
            dfs(i + 1, cur)
            dfs(i + 1, cur + toppingCosts[i])
            dfs(i + 1, cur + 2 * toppingCosts[i])
        }

        for base in baseCosts {
            dfs(0, base)
        }
        return best
    }
}
