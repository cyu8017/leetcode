// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

import "sort"

func highFive(items [][]int) [][]int {
	scores := map[int][]int{}
	for _, item := range items {
		scores[item[0]] = append(scores[item[0]], item[1])
	}
	ids := make([]int, 0, len(scores))
	for id := range scores {
		ids = append(ids, id)
	}
	sort.Ints(ids)
	ans := make([][]int, 0, len(ids))
	for _, id := range ids {
		top := append([]int(nil), scores[id]...)
		sort.Sort(sort.Reverse(sort.IntSlice(top)))
		sum := 0
		for i := 0; i < 5; i++ {
			sum += top[i]
		}
		ans = append(ans, []int{id, sum / 5})
	}
	return ans
}
