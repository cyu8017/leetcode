// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

func missingRolls(rolls []int, mean int, n int) []int {
	sum := 0
	for _, r := range rolls {
		sum += r
	}
	remain := mean*(len(rolls)+n) - sum
	if remain < n || remain > 6*n {
		return []int{}
	}
	ans := make([]int, n)
	base, extra := remain/n, remain%n
	for i := 0; i < n; i++ {
		ans[i] = base
		if i < extra {
			ans[i]++
		}
	}
	return ans
}
