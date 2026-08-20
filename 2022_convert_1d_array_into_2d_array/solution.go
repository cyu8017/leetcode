// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

func construct2DArray(original []int, m int, n int) [][]int {
	if len(original) != m*n {
		return [][]int{}
	}
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = original[i*n : (i+1)*n]
	}
	return ans
}
