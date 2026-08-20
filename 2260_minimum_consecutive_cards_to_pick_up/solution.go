// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

func minimumCardPickup(cards []int) int {
	last := map[int]int{}
	ans := -1
	for i, c := range cards {
		if j, ok := last[c]; ok {
			diff := i - j + 1
			if ans == -1 || diff < ans {
				ans = diff
			}
		}
		last[c] = i
	}
	return ans
}
