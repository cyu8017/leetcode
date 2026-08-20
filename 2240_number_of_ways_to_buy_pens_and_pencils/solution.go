// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

func waysToBuyPensPencils(total int, cost1 int, cost2 int) int64 {
	var ans int64
	for pens := 0; pens*cost1 <= total; pens++ {
		remain := total - pens*cost1
		ans += int64(remain/cost2) + 1
	}
	return ans
}
