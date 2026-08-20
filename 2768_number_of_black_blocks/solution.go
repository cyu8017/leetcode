// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

func countBlackBlocks(m int, n int, coordinates [][]int) []int64 {
	cnt := map[[2]int]int{}
	for _, c := range coordinates {
		x, y := c[0], c[1]
		for i := x - 1; i <= x; i++ {
			for j := y - 1; j <= y; j++ {
				if i >= 0 && j >= 0 && i < m-1 && j < n-1 {
					cnt[[2]int{i, j}]++
				}
			}
		}
	}
	ans := make([]int64, 5)
	total := int64(m-1) * int64(n-1)
	ans[0] = total
	for _, v := range cnt {
		ans[v]++
		ans[0]--
	}
	return ans
}
