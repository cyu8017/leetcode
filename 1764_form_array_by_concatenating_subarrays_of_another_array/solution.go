// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

func canChoose(groups [][]int, nums []int) bool {
	n := len(nums)
	matches := func(start int, g []int) bool {
		for t := 0; t < len(g); t++ {
			if nums[start+t] != g[t] {
				return false
			}
		}
		return true
	}
	var dfs func(i, start int) bool
	dfs = func(i, start int) bool {
		if i == len(groups) {
			return start == n
		}
		g := groups[i]
		m := len(g)
		for j := start; j <= n-m; j++ {
			if matches(j, g) && dfs(i+1, j+m) {
				return true
			}
		}
		return false
	}
	return dfs(0, 0)
}
