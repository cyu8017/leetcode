// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

func getLastMoment(n int, left []int, right []int) int {
	ans := 0
	for _, x := range left {
		if x > ans {
			ans = x
		}
	}
	for _, x := range right {
		if n-x > ans {
			ans = n - x
		}
	}
	return ans
}
