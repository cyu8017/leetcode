// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

func maxValueAfterReverse(nums []int) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	base := 0
	for i := 0; i+1 < len(nums); i++ {
		base += abs(nums[i] - nums[i+1])
	}
	gain := 0
	low, high := int(1e9), int(-1e9)
	for i := 0; i+1 < len(nums); i++ {
		a, b := nums[i], nums[i+1]
		g1 := abs(nums[0]-b) - abs(a-b)
		g2 := abs(nums[len(nums)-1]-a) - abs(a-b)
		if g1 > gain {
			gain = g1
		}
		if g2 > gain {
			gain = g2
		}
		mx, mn := a, b
		if b > a {
			mx, mn = b, a
		}
		if mx < low {
			low = mx
		}
		if mn > high {
			high = mn
		}
	}
	alt := 2 * (high - low)
	if alt > gain {
		gain = alt
	}
	return base + gain
}
