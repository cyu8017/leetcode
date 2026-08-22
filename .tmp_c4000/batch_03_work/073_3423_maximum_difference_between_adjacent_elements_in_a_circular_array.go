// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

func maxAdjacentDistance(nums []int) int {
	ans := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		d := nums[i] - nums[(i+1)%n]
		if d < 0 {
			d = -d
		}
		if d > ans {
			ans = d
		}
	}
	return ans
}
