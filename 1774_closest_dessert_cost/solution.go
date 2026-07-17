// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

func closestCost(baseCosts []int, toppingCosts []int, target int) int {
    best := 1 << 29
    abs := func(x int) int {
        if x < 0 {
            return -x
        }
        return x
    }
    var dfs func(i, cur int)
    dfs = func(i, cur int) {
        curDiff := abs(cur - target)
        bestDiff := abs(best - target)
        if curDiff < bestDiff || (curDiff == bestDiff && cur < best) {
            best = cur
        }
        if i == len(toppingCosts) || cur >= target {
            return
        }
        dfs(i+1, cur)
        dfs(i+1, cur+toppingCosts[i])
        dfs(i+1, cur+2*toppingCosts[i])
    }
    for _, base := range baseCosts {
        dfs(0, base)
    }
    return best
}
