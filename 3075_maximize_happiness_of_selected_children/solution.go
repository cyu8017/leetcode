// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

func maximumHappinessSum(happiness []int, k int) (ans int64) {
	sort.Ints(happiness)
	for i := 0; i < k; i++ {
		x := happiness[len(happiness)-i-1] - i
		ans += int64(max(x, 0))
	}
	return
}
