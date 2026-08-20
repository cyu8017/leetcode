// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

func minimumCosts(regular []int, express []int, expressCost int) []int64 {
	n := len(regular)
	ans := make([]int64, n)
	reg, exp := int64(0), int64(expressCost)
	for i := 0; i < n; i++ {
		nextReg := min64(reg+int64(regular[i]), exp+int64(express[i]))
		nextExp := min64(reg+int64(regular[i])+int64(expressCost), exp+int64(express[i]))
		reg, exp = nextReg, nextExp
		ans[i] = min64(reg, exp)
	}
	return ans
}

func min64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}
