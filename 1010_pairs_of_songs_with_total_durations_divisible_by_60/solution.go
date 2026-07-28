// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

func numPairsDivisibleBy60(time []int) int {
	count := make([]int, 60)
	ans := 0
	for _, t := range time {
		ans += count[(60-t%60)%60]
		count[t%60]++
	}
	return ans
}
