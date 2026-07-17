// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

func minOperations(boxes string) []int {
    n := len(boxes)
    ans := make([]int, n)
    balls, ops := 0, 0
    for i := 1; i < n; i++ {
        balls += int(boxes[i-1] - '0')
        ops += balls
        ans[i] = ops
    }
    balls, ops = 0, 0
    for i := n - 2; i >= 0; i-- {
        balls += int(boxes[i+1] - '0')
        ops += balls
        ans[i] += ops
    }
    return ans
}
