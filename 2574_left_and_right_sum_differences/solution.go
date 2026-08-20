// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/


func leftRightDifference(nums []int) []int {
	total := 0
	for _, x := range nums {
		total += x
	}
	ans := make([]int, len(nums))
	left := 0
	for i, x := range nums {
		right := total - left - x
		d := left - right
		if d < 0 {
			d = -d
		}
		ans[i] = d
		left += x
	}
	return ans
}
