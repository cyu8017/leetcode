// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

import "sort"
import "strings"

func topStudents(positive_feedback []string, negative_feedback []string, report []string, student_id []int, k int) []int {
	pos := map[string]bool{}
	neg := map[string]bool{}
	for _, w := range positive_feedback {
		pos[w] = true
	}
	for _, w := range negative_feedback {
		neg[w] = true
	}
	type pair struct{ id, score int }
	arr := make([]pair, len(report))
	for i, r := range report {
		score := 0
		for _, w := range strings.Fields(r) {
			if pos[w] {
				score += 3
			} else if neg[w] {
				score--
			}
		}
		arr[i] = pair{student_id[i], score}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].score != arr[j].score {
			return arr[i].score > arr[j].score
		}
		return arr[i].id < arr[j].id
	})
	ans := make([]int, k)
	for i := 0; i < k; i++ {
		ans[i] = arr[i].id
	}
	return ans
}
