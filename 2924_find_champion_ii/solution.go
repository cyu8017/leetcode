// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

func findChampion(n int, edges [][]int) int {
	indeg := make([]int, n)
	for _, e := range edges {
		indeg[e[1]]++
	}
	ans := -1
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			if ans != -1 {
				return -1
			}
			ans = i
		}
	}
	return ans
}
