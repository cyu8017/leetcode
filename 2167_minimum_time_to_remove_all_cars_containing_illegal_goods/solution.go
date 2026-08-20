// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

func minimumTime(s string) int {
	n := len(s)
	left := make([]int, n)
	if s[0] == '1' {
		left[0] = 1
	}
	for i := 1; i < n; i++ {
		left[i] = left[i-1]
		if s[i] == '1' {
			cand := left[i-1] + 2
			if i+1 < cand {
				left[i] = i + 1
			} else {
				left[i] = cand
			}
		}
	}
	ans := left[n-1]
	right := 0
	for i := n - 1; i >= 0; i-- {
		if s[i] == '1' {
			cand := right + 2
			if n-i < cand {
				right = n - i
			} else {
				right = cand
			}
		}
		leftCost := 0
		if i > 0 {
			leftCost = left[i-1]
		}
		if leftCost+right < ans {
			ans = leftCost + right
		}
	}
	return ans
}
