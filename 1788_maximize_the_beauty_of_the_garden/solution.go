// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

func maximumBeauty(flowers []int) int {
	first := make(map[int]int)
	prefix := make([]int, len(flowers)+1)
	for i, value := range flowers {
		positive := value
		if positive < 0 {
			positive = 0
		}
		prefix[i+1] = prefix[i] + positive
	}
	best := int(-1) << 62
	for i, value := range flowers {
		if left, ok := first[value]; ok {
			between := prefix[i] - prefix[left+1]
			candidate := flowers[left] + flowers[i] + between
			if candidate > best {
				best = candidate
			}
		} else {
			first[value] = i
		}
	}
	return best
}
