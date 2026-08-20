// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

import "sort"

func maximumLength(s string) int {
	groups := [26][]int{}
	n := len(s)
	for i := 0; i < n; {
		j := i
		for j < n && s[j] == s[i] {
			j++
		}
		groups[s[i]-'a'] = append(groups[s[i]-'a'], j-i)
		i = j
	}
	ans := -1
	for c := 0; c < 26; c++ {
		arr := groups[c]
		if len(arr) == 0 {
			continue
		}
		sort.Slice(arr, func(i, j int) bool { return arr[i] > arr[j] })
		for L := arr[0]; L >= 1; L-- {
			cnt := 0
			for _, g := range arr {
				if g >= L {
					cnt += g - L + 1
				}
			}
			if cnt >= 3 {
				if L > ans {
					ans = L
				}
				break
			}
		}
	}
	return ans
}
