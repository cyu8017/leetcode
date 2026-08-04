// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

func maxProduct(s string) int64 {
	n := len(s)
	radius := make([]int, n)
	center, right := 0, 0
	for i := 0; i < n; i++ {
		if i < right {
			mir := 2*center - i
			if right-i < radius[mir] {
				radius[i] = right - i
			} else {
				radius[i] = radius[mir]
			}
		}
		for i-radius[i]-1 >= 0 && i+radius[i]+1 < n && s[i-radius[i]-1] == s[i+radius[i]+1] {
			radius[i]++
		}
		if i+radius[i] > right {
			center, right = i, i+radius[i]
		}
	}
	end := make([]int, n)
	start := make([]int, n)
	for i := range end {
		end[i], start[i] = 1, 1
	}
	for i := 0; i < n; i++ {
		r := radius[i]
		if 2*r+1 > end[i+r] {
			end[i+r] = 2*r + 1
		}
		if 2*r+1 > start[i-r] {
			start[i-r] = 2*r + 1
		}
	}
	for i := n - 2; i >= 0; i-- {
		if end[i+1]-2 > end[i] {
			end[i] = end[i+1] - 2
		}
	}
	for i := 1; i < n; i++ {
		if start[i-1]-2 > start[i] {
			start[i] = start[i-1] - 2
		}
	}
	pre := make([]int, n)
	pre[0] = end[0]
	for i := 1; i < n; i++ {
		pre[i] = pre[i-1]
		if end[i] > pre[i] {
			pre[i] = end[i]
		}
	}
	suf := make([]int, n)
	suf[n-1] = start[n-1]
	for i := n - 2; i >= 0; i-- {
		suf[i] = suf[i+1]
		if start[i] > suf[i] {
			suf[i] = start[i]
		}
	}
	var best int64
	for i := 0; i < n-1; i++ {
		prod := int64(pre[i]) * int64(suf[i+1])
		if prod > best {
			best = prod
		}
	}
	return best
}
