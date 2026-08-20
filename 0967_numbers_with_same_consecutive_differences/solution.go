// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

func numsSameConsecDiff(n int, k int) []int {
	ans := []int{}
	var dfs func(num, length int)
	dfs = func(num, length int) {
		if length == n {
			ans = append(ans, num)
			return
		}
		last := num % 10
		candidates := map[int]bool{last + k: true, last - k: true}
		for nxt := range candidates {
			if nxt >= 0 && nxt <= 9 {
				dfs(num*10+nxt, length+1)
			}
		}
	}
	for start := 1; start <= 9; start++ {
		dfs(start, 1)
	}
	return ans
}
