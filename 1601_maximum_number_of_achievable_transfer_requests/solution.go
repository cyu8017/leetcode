// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

func maximumRequests(n int, requests [][]int) int {
	ans := 0
	m := len(requests)
	for mask := 0; mask < 1<<m; mask++ {
		cnt := 0
		for t := mask; t > 0; t &= t - 1 {
			cnt++
		}
		if cnt <= ans {
			continue
		}
		bal := make([]int, n)
		for i, req := range requests {
			if mask>>i&1 == 1 {
				bal[req[0]]--
				bal[req[1]]++
			}
		}
		ok := true
		for _, v := range bal {
			if v != 0 {
				ok = false
				break
			}
		}
		if ok {
			ans = cnt
		}
	}
	return ans
}
