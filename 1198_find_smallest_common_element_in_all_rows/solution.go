// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

func smallestCommonElement(mat [][]int) int {
	common := map[int]bool{}
	for _, x := range mat[0] {
		common[x] = true
	}
	for _, row := range mat[1:] {
		next := map[int]bool{}
		for _, x := range row {
			if common[x] {
				next[x] = true
			}
		}
		common = next
		if len(common) == 0 {
			return -1
		}
	}
	ans := int(^uint(0) >> 1)
	for x := range common {
		if x < ans {
			ans = x
		}
	}
	return ans
}
