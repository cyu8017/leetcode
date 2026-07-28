// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

func maxScoreSightseeingPair(values []int) int {
	best := values[0]
	ans := 0
	for j := 1; j < len(values); j++ {
		if best+values[j]-j > ans {
			ans = best + values[j] - j
		}
		if values[j]+j > best {
			best = values[j] + j
		}
	}
	return ans
}
