// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

func shortestSequence(rolls []int, k int) int {
	seen := map[int]bool{}
	ans := 1
	for _, r := range rolls {
		seen[r] = true
		if len(seen) == k {
			ans++
			seen = map[int]bool{}
		}
	}
	return ans
}
