// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

func removeInterval(intervals [][]int, toBeRemoved []int) [][]int {
	left, right := toBeRemoved[0], toBeRemoved[1]
	ans := [][]int{}
	for _, iv := range intervals {
		start, end := iv[0], iv[1]
		if end <= left || start >= right {
			ans = append(ans, []int{start, end})
		} else {
			if start < left {
				ans = append(ans, []int{start, left})
			}
			if end > right {
				ans = append(ans, []int{right, end})
			}
		}
	}
	return ans
}
