// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

func maximumScore(nums []int, multipliers []int) int {
    n := len(nums)
    m := len(multipliers)
    next := make([]int, m+1)
    for i := m - 1; i >= 0; i-- {
        cur := make([]int, m+1)
        for left := i; left >= 0; left-- {
            right := n - 1 - (i - left)
            takeLeft := nums[left]*multipliers[i] + next[left+1]
            takeRight := nums[right]*multipliers[i] + next[left]
            if takeLeft > takeRight {
                cur[left] = takeLeft
            } else {
                cur[left] = takeRight
            }
        }
        next = cur
    }
    return next[0]
}
