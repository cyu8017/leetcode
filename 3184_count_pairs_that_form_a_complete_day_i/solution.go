// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

func countCompleteDayPairs(hours []int) (ans int) {
	cnt := [24]int{}
	for _, x := range hours {
		ans += cnt[(24-x%24)%24]
		cnt[x%24]++
	}
	return
}
