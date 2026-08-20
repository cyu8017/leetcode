// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

func minOperations(nums []int) int {
	ops := 0
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] <= nums[i+1] {
			continue
		}
		// divide nums[i] by proper divisor until <= nums[i+1]
		for nums[i] > nums[i+1] {
			d := smallestProperDivisor(nums[i])
			if d == nums[i] {
				return -1
			}
			nums[i] /= d
			ops++
			if nums[i] > nums[i+1] && smallestProperDivisor(nums[i]) == nums[i] {
				return -1
			}
		}
	}
	return ops
}

func smallestProperDivisor(x int) int {
	for d := 2; d*d <= x; d++ {
		if x%d == 0 {
			return d
		}
	}
	return x
}
