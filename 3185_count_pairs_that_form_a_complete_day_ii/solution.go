// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

func countCompleteDayPairs(hours []int) (ans int64) {
	cnt := [24]int{}
	for _, x := range hours {
		ans += int64(cnt[(24-x%24)%24])
		cnt[x%24]++
	}
	return
}
