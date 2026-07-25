// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

func maximumUniqueSubarray(nums []int) int {
	seen := map[int]int{}
	left, cur, best := 0, 0, 0
	for right, x := range nums {
		if idx, ok := seen[x]; ok && idx >= left {
			for left <= idx {
				cur -= nums[left]
				left++
			}
		}
		seen[x] = right
		cur += x
		if cur > best {
			best = cur
		}
	}
	return best
}
