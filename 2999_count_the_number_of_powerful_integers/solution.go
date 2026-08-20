// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

import "strconv"

func numberOfPowerfulInt(start, finish int64, limit int, s string) int64 {
	count := func(num int64) int64 {
		if num < 0 {
			return 0
		}
		t := strconv.FormatInt(num, 10)
		sn := len(s)
		if len(t) < sn {
			return 0
		}
		var dfs func(pos int, tight bool, memo map[[2]int]int64) int64
		dfs = func(pos int, tight bool, memo map[[2]int]int64) int64 {
			if pos == len(t)-sn {
				suffix := t[pos:]
				if tight {
					if suffix >= s {
						return 1
					}
					return 0
				}
				return 1
			}
			key := [2]int{pos, 0}
			if tight {
				key[1] = 1
			}
			if v, ok := memo[key]; ok {
				return v
			}
			up := limit
			if tight {
				up = int(t[pos] - '0')
				if up > limit {
					up = limit
				}
			}
			var ans int64
			for d := 0; d <= up; d++ {
				nt := tight && d == int(t[pos]-'0')
				ans += dfs(pos+1, nt, memo)
			}
			memo[key] = ans
			return ans
		}
		// numbers with fewer digits
		var ans int64
		for length := sn; length < len(t); length++ {
			preLen := length - sn
			var ways int64 = 1
			if preLen > 0 {
				ways = int64(limit)
				for i := 1; i < preLen; i++ {
					ways *= int64(limit + 1)
				}
			}
			ans += ways
		}
		ans += dfs(0, true, map[[2]int]int64{})
		return ans
	}
	return count(finish) - count(start-1)
}
