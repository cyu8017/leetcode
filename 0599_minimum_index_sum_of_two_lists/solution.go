// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

func findRestaurant(list1 []string, list2 []string) []string {
	index1 := map[string]int{}
	for i, name := range list1 {
		index1[name] = i
	}
	best := int(^uint(0) >> 1)
	answer := []string{}
	for j, name := range list2 {
		i, ok := index1[name]
		if !ok {
			continue
		}
		total := i + j
		if total < best {
			best = total
			answer = []string{name}
		} else if total == best {
			answer = append(answer, name)
		}
	}
	return answer
}
