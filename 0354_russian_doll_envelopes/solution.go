// LeetCode 0354 - Russian Doll Envelopes
// https://leetcode.com/problems/russian-doll-envelopes/

import "sort"

func maxEnvelopes(envelopes [][]int) int {
	sort.Slice(envelopes, func(i, j int) bool {
		if envelopes[i][0] != envelopes[j][0] {
			return envelopes[i][0] < envelopes[j][0]
		}
		return envelopes[i][1] > envelopes[j][1]
	})

	tails := make([]int, 0)
	for _, envelope := range envelopes {
		height := envelope[1]
		left, right := 0, len(tails)
		for left < right {
			mid := left + (right-left)/2
			if tails[mid] < height {
				left = mid + 1
			} else {
				right = mid
			}
		}
		if left == len(tails) {
			tails = append(tails, height)
		} else {
			tails[left] = height
		}
	}

	return len(tails)
}
