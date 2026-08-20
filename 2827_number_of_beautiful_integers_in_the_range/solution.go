// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

import "strconv"

func numberOfBeautifulIntegers(low int, high int, k int) int {
	var count func(int) int
	count = func(n int) int {
		if n < 0 {
			return 0
		}
		s := strconv.Itoa(n)
		var dfs func(pos int, diff int, mod int, tight bool, started bool, memo map[[5]int]int) int
		dfs = func(pos, diff, mod int, tight, started bool, memo map[[5]int]int) int {
			if pos == len(s) {
				if started && diff == 0 && mod == 0 {
					return 1
				}
				return 0
			}
			key := [5]int{pos, diff + 20, mod, 0, 0}
			if tight {
				key[3] = 1
			}
			if started {
				key[4] = 1
			}
			if v, ok := memo[key]; ok {
				return v
			}
			up := 9
			if tight {
				up = int(s[pos] - '0')
			}
			ans := 0
			for d := 0; d <= up; d++ {
				nt := tight && d == up
				if !started {
					if d == 0 {
						ans += dfs(pos+1, diff, mod, nt, false, memo)
					} else {
						nd := diff
						if d%2 == 0 {
							nd++
						} else {
							nd--
						}
						ans += dfs(pos+1, nd, d%k, nt, true, memo)
					}
				} else {
					nd := diff
					if d%2 == 0 {
						nd++
					} else {
						nd--
					}
					ans += dfs(pos+1, nd, (mod*10+d)%k, nt, true, memo)
				}
			}
			memo[key] = ans
			return ans
		}
		return dfs(0, 0, 0, true, false, map[[5]int]int{})
	}
	return count(high) - count(low-1)
}
