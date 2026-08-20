// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

func distributeCookies(cookies []int, k int) int {
	n := len(cookies)
	bags := make([]int, k)
	ans := 1 << 30
	var dfs func(int)
	dfs = func(i int) {
		if i == n {
			mx := 0
			for _, b := range bags {
				if b > mx {
					mx = b
				}
			}
			if mx < ans {
				ans = mx
			}
			return
		}
		seen := map[int]bool{}
		for j := 0; j < k; j++ {
			if seen[bags[j]] {
				continue
			}
			seen[bags[j]] = true
			bags[j] += cookies[i]
			if bags[j] < ans {
				dfs(i + 1)
			}
			bags[j] -= cookies[i]
			if bags[j] == 0 {
				break
			}
		}
	}
	dfs(0)
	return ans
}
