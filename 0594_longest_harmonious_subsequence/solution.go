// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

func findLHS(nums []int) int {
	counts := map[int]int{}
	for _, num := range nums {
		counts[num]++
	}
	best := 0
	for value, count := range counts {
		if next, ok := counts[value+1]; ok {
			if count+next > best {
				best = count + next
			}
		}
	}
	return best
}
