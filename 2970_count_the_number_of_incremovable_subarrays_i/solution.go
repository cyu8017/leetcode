// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

func incremovableSubarrayCount(nums []int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			prev := -1
			ok := true
			for t := 0; t < n; t++ {
				if t >= i && t <= j {
					continue
				}
				if nums[t] <= prev {
					ok = false
					break
				}
				prev = nums[t]
			}
			if ok {
				ans++
			}
		}
	}
	return ans
}
