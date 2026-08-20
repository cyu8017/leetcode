// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/


func distinctDifferenceArray(nums []int) []int {
	n := len(nums)
	suf := make([]int, n+1)
	seen := map[int]bool{}
	for i := n - 1; i >= 0; i-- {
		seen[nums[i]] = true
		suf[i] = len(seen)
	}
	seen = map[int]bool{}
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		seen[nums[i]] = true
		ans[i] = len(seen) - suf[i+1]
	}
	return ans
}
