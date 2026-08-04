// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

func addRungs(rungs []int, dist int) int {
	prev := 0
	ans := 0
	for _, r := range rungs {
		gap := r - prev
		if gap > dist {
			ans += (gap - 1) / dist
		}
		prev = r
	}
	return ans
}
