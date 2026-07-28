// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

func lastStoneWeightII(stones []int) int {
	total := 0
	for _, s := range stones {
		total += s
	}
	reachable := map[int]bool{0: true}
	for _, stone := range stones {
		next := map[int]bool{}
		for s := range reachable {
			next[s] = true
			next[s+stone] = true
		}
		reachable = next
	}
	best := total
	for s := range reachable {
		diff := total - 2*s
		if diff < 0 {
			diff = -diff
		}
		if diff < best {
			best = diff
		}
	}
	return best
}
