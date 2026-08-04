// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

import "sort"

func groupThePeople(groupSizes []int) [][]int {
	pending := map[int][]int{}
	answer := [][]int{}
	for person, size := range groupSizes {
		pending[size] = append(pending[size], person)
		if len(pending[size]) == size {
			answer = append(answer, pending[size])
			pending[size] = nil
		}
	}
	sort.Slice(answer, func(i, j int) bool {
		if len(answer[i]) != len(answer[j]) {
			return len(answer[i]) < len(answer[j])
		}
		for k := 0; k < len(answer[i]); k++ {
			if answer[i][k] != answer[j][k] {
				return answer[i][k] < answer[j][k]
			}
		}
		return false
	})
	return answer
}
