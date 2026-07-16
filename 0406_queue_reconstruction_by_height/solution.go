// LeetCode 0406 - Queue Reconstruction by Height
// https://leetcode.com/problems/queue-reconstruction-by-height/

import "sort"

func reconstructQueue(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] != people[j][0] {
			return people[i][0] > people[j][0]
		}
		return people[i][1] < people[j][1]
	})

	queue := make([][]int, 0, len(people))
	for _, person := range people {
		index := person[1]
		queue = append(queue, nil)
		copy(queue[index+1:], queue[index:])
		queue[index] = person
	}

	return queue
}
