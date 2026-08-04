// LeetCode 1504 - Count Submatrices with All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

func numSubmat(mat [][]int) int {
	ans := 0
	heights := make([]int, len(mat[0]))
	for _, row := range mat {
		for j, x := range row {
			if x == 0 {
				heights[j] = 0
			} else {
				heights[j]++
			}
		}
		type pair struct{ h, count int }
		stack := []pair{}
		running := 0
		for _, h := range heights {
			count := 1
			for len(stack) > 0 && stack[len(stack)-1].h >= h {
				old := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				running -= old.h * old.count
				count += old.count
			}
			stack = append(stack, pair{h, count})
			running += h * count
			ans += running
		}
	}
	return ans
}
