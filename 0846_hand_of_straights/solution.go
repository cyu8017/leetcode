// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

import "sort"

func isNStraightHand(hand []int, groupSize int) bool {
	if len(hand)%groupSize != 0 {
		return false
	}
	count := map[int]int{}
	for _, v := range hand {
		count[v]++
	}
	keys := make([]int, 0, len(count))
	for k := range count {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, start := range keys {
		for count[start] > 0 {
			for x := start; x < start+groupSize; x++ {
				if count[x] == 0 {
					return false
				}
				count[x]--
			}
		}
	}
	return true
}
