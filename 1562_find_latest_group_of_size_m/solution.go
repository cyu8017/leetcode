// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

func findLatestStep(arr []int, m int) int {
	if m == len(arr) {
		return m
	}
	lengths := map[int]int{}
	answer := -1
	for step, x := range arr {
		step++
		left, right := lengths[x-1], lengths[x+1]
		size := left + 1 + right
		lengths[x-left] = size
		lengths[x+right] = size
		if left == m || right == m {
			answer = step - 1
		}
	}
	return answer
}
