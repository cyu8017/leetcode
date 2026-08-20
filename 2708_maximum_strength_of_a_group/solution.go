// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/


import "sort"

func maxStrength(nums []int) int64 {
	sort.Ints(nums)
	n := len(nums)
	if n == 1 {
		return int64(nums[0])
	}
	prod := int64(1)
	used := false
	i := 0
	for i+1 < n && nums[i] < 0 && nums[i+1] < 0 {
		prod *= int64(nums[i]) * int64(nums[i+1])
		used = true
		i += 2
	}
	negLeft := i < n && nums[i] < 0
	for ; i < n; i++ {
		if nums[i] > 0 {
			prod *= int64(nums[i])
			used = true
		}
	}
	if !used {
		// only zeros and maybe one negative
		if negLeft {
			for _, x := range nums {
				if x == 0 {
					return 0
				}
			}
			return int64(nums[n-1])
		}
		return 0
	}
	return prod
}
