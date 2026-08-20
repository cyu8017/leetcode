// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

func arrayChange(nums []int, operations [][]int) []int {
	pos := map[int]int{}
	for i, v := range nums {
		pos[v] = i
	}
	for _, op := range operations {
		i := pos[op[0]]
		nums[i] = op[1]
		delete(pos, op[0])
		pos[op[1]] = i
	}
	return nums
}
