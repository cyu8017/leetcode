// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

func minOperations(nums []int, x int) int {
	total := 0
	for _, v := range nums {
		total += v
	}
	target := total - x
	if target < 0 {
		return -1
	}
	best, left, cur := -1, 0, 0
	for right, v := range nums {
		cur += v
		for cur > target {
			cur -= nums[left]
			left++
		}
		if cur == target && right-left+1 > best {
			best = right - left + 1
		}
	}
	if best < 0 {
		return -1
	}
	return len(nums) - best
}
