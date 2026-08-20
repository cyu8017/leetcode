// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/


func rowAndMaximumOnes(mat [][]int) []int {
	bestRow, bestCnt := 0, -1
	for i, row := range mat {
		cnt := 0
		for _, v := range row {
			cnt += v
		}
		if cnt > bestCnt {
			bestCnt = cnt
			bestRow = i
		}
	}
	return []int{bestRow, bestCnt}
}
