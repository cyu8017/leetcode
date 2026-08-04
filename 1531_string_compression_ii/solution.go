// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

func getLengthOfOptimalCompression(s string, k int) int {
	n := len(s)
	const inf = 1_000_000_000
	memo := map[[2]int]int{}
	var dp func(index, remaining int) int
	dp = func(index, remaining int) int {
		if remaining < 0 {
			return inf
		}
		if index == n || n-index <= remaining {
			return 0
		}
		key := [2]int{index, remaining}
		if v, ok := memo[key]; ok {
			return v
		}
		answer := dp(index+1, remaining-1)
		same, removed := 0, 0
		for j := index; j < n; j++ {
			if s[j] == s[index] {
				same++
				encoded := 1
				if same >= 2 {
					encoded++
				}
				if same >= 10 {
					encoded++
				}
				if same >= 100 {
					encoded++
				}
				cand := encoded + dp(j+1, remaining-removed)
				if cand < answer {
					answer = cand
				}
			} else {
				removed++
				if removed > remaining {
					break
				}
			}
		}
		memo[key] = answer
		return answer
	}
	return dp(0, k)
}
