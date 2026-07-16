// LeetCode 0330 - Patching Array
// https://leetcode.com/problems/patching-array/

func minPatches(nums []int, n int) int {
	patches := 0
	miss := int64(1)
	index := 0
	for miss <= int64(n) {
		if index < len(nums) && int64(nums[index]) <= miss {
			miss += int64(nums[index])
			index++
		} else {
			miss += miss
			patches++
		}
	}
	return patches
}
