// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

func elementInNums(nums []int, queries [][]int) []int {
	n := len(nums)
	ans := make([]int, len(queries))
	for i, q := range queries {
		t, idx := q[0], q[1]
		cycle := t % (2 * n)
		var size, offset int
		if cycle < n {
			size = n - cycle
			offset = cycle
		} else {
			size = cycle - n
			offset = 0
		}
		if idx >= size {
			ans[i] = -1
		} else {
			ans[i] = nums[offset+idx]
		}
	}
	return ans
}
