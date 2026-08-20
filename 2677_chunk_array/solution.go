// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/


func chunk(arr []int, size int) [][]int {
	ans := [][]int{}
	for i := 0; i < len(arr); i += size {
		end := i + size
		if end > len(arr) {
			end = len(arr)
		}
		ans = append(ans, append([]int{}, arr[i:end]...))
	}
	return ans
}
