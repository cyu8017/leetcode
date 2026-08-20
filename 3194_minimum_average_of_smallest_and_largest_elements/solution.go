// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

func minimumAverage(nums []int) float64 {
	sort.Ints(nums)
	n := len(nums)
	ans := 1 << 30
	for i, x := range nums[:n/2] {
		ans = min(ans, x+nums[n-i-1])
	}
	return float64(ans) / 2
}
