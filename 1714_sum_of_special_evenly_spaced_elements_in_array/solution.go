// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

func solve(nums []int, queries [][]int) []int {
    const mod = 1000000007
    n := len(nums)
    block := 1
    for block*block <= n {
        block++
    }
    dp := make([][]int, block)
    for step := range dp {
        dp[step] = make([]int, n)
    }
    for step := 1; step < block; step++ {
        for i := n - 1; i >= 0; i-- {
            next := 0
            if i+step < n {
                next = dp[step][i+step]
            }
            dp[step][i] = (nums[i] + next) % mod
        }
    }
    ans := make([]int, 0, len(queries))
    for _, query := range queries {
        start, step := query[0], query[1]
        if step < block {
            ans = append(ans, dp[step][start])
        } else {
            total := 0
            for i := start; i < n; i += step {
                total += nums[i]
            }
            ans = append(ans, total%mod)
        }
    }
    return ans
}
