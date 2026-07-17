// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

import "sort"

func reductionOperations(nums []int) int {
	sorted := append([]int(nil), nums...)
	sort.Ints(sorted)

	answer := 0
	rank := 0
	for i := 1; i < len(sorted); i++ {
		if sorted[i] != sorted[i-1] {
			rank++
		}
		answer += rank
	}
	return answer
}
