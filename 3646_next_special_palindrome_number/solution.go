// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

import (
	"fmt"
	"sort"
)

func specialPalindrome(n int64) int64 {
	cands := []int64{}
	var gen func(mask int)
	gen = func(mask int) {
		total := 0
		odd := 0
		for d := 1; d <= 9; d++ {
			if mask>>d&1 == 1 {
				total += d
				if d%2 == 1 {
					odd++
				}
			}
		}
		if total == 0 || total > 18 || odd > 1 {
			return
		}
		halfCnt := [10]int{}
		mid := 0
		for d := 1; d <= 9; d++ {
			if mask>>d&1 == 0 {
				continue
			}
			halfCnt[d] = d / 2
			if d%2 == 1 {
				mid = d
			}
		}
		halfLen := total / 2
		var dfs func(pos int, cur []int)
		dfs = func(pos int, cur []int) {
			if pos == halfLen {
				left := ""
				for _, x := range cur {
					left += string(rune('0' + x))
				}
				s := left
				if mid > 0 {
					s += string(rune('0' + mid))
				}
				for i := len(left) - 1; i >= 0; i-- {
					s += string(left[i])
				}
				var val int64
				fmt.Sscan(s, &val)
				cands = append(cands, val)
				return
			}
			for d := 1; d <= 9; d++ {
				if halfCnt[d] == 0 {
					continue
				}
				halfCnt[d]--
				dfs(pos+1, append(append([]int{}, cur...), d))
				halfCnt[d]++
			}
		}
		dfs(0, nil)
	}
	for mask := 1; mask < 1<<10; mask++ {
		if mask&1 == 1 {
			continue
		}
		gen(mask)
	}
	sort.Slice(cands, func(i, j int) bool { return cands[i] < cands[j] })
	for _, v := range cands {
		if v > n {
			return v
		}
	}
	return -1
}
