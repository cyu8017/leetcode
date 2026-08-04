// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
	owned := map[int]bool{}
	opened := map[int]bool{}
	q := []int{}
	for _, box := range initialBoxes {
		owned[box] = true
		if status[box] == 1 {
			q = append(q, box)
		}
	}
	total := 0
	for len(q) > 0 {
		box := q[0]
		q = q[1:]
		if opened[box] || status[box] == 0 {
			continue
		}
		opened[box] = true
		total += candies[box]
		for _, key := range keys[box] {
			status[key] = 1
			if owned[key] && !opened[key] {
				q = append(q, key)
			}
		}
		for _, child := range containedBoxes[box] {
			owned[child] = true
			if status[child] == 1 && !opened[child] {
				q = append(q, child)
			}
		}
	}
	return total
}
