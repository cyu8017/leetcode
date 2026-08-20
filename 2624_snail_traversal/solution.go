// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/


func snail(nums []int, rowsCount, colsCount int) [][]int {
	if rowsCount*colsCount != len(nums) {
		return [][]int{}
	}
	ans := make([][]int, rowsCount)
	for i := range ans {
		ans[i] = make([]int, colsCount)
	}
	idx := 0
	for c := 0; c < colsCount; c++ {
		if c%2 == 0 {
			for r := 0; r < rowsCount; r++ {
				ans[r][c] = nums[idx]
				idx++
			}
		} else {
			for r := rowsCount - 1; r >= 0; r-- {
				ans[r][c] = nums[idx]
				idx++
			}
		}
	}
	return ans
}
