// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

func distributeCandies(candyType []int) int {
	seen := map[int]struct{}{}
	for _, c := range candyType {
		seen[c] = struct{}{}
	}
	limit := len(candyType) / 2
	if len(seen) < limit {
		return len(seen)
	}
	return limit
}
