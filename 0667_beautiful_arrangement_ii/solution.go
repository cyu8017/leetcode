// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

func constructArray(n int, k int) []int {
	res := make([]int, 0, n)
	for i := 1; i <= n-k; i++ {
		res = append(res, i)
	}
	left, right := n-k+1, n
	takeHigh := true
	for left <= right {
		if takeHigh {
			res = append(res, right)
			right--
		} else {
			res = append(res, left)
			left++
		}
		takeHigh = !takeHigh
	}
	return res
}
