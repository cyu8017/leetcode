// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

func bestClosingTime(customers string) int {
	n := len(customers)
	penalty := 0
	for i := 0; i < n; i++ {
		if customers[i] == 'Y' {
			penalty++
		}
	}
	best, ans := penalty, 0
	for i := 0; i < n; i++ {
		if customers[i] == 'Y' {
			penalty--
		} else {
			penalty++
		}
		if penalty < best {
			best = penalty
			ans = i + 1
		}
	}
	return ans
}
