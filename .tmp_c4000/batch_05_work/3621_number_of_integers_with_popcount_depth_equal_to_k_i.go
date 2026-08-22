// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

import "math/bits"

func popcountDepth(n int64, k int) int64 {
	if k == 0 {
		if n >= 1 {
			return 1
		}
		return 0
	}
	depth := func(x int) int {
		if x <= 0 {
			return 100
		}
		d := 0
		for x > 1 {
			x = bits.OnesCount(uint(x))
			d++
		}
		return d
	}
	// Digit DP on binary representation
	s := ""
	for x := n; x > 0; x >>= 1 {
		s = string(rune('0'+(x&1))) + s
	}
	if s == "" {
		s = "0"
	}
	type key struct{ pos, tight, started, pc int }
	memo := map[key]int64{}
	var dfs func(pos, tight, started, pc int) int64
	dfs = func(pos, tight, started, pc int) int64 {
		if pos == len(s) {
			if started == 0 {
				return 0
			}
			// number has popcount == pc; depth(number)==k
			if pc == 1 {
				return bool64(k == 1)
			}
			return bool64(depth(pc) == k-1)
		}
		kk := key{pos, tight, started, pc}
		if v, ok := memo[kk]; ok {
			return v
		}
		up := 1
		if tight == 1 {
			up = int(s[pos] - '0')
		}
		var res int64
		for dig := 0; dig <= up; dig++ {
			nt := 0
			if tight == 1 && dig == up {
				nt = 1
			}
			if started == 0 && dig == 0 {
				res += dfs(pos+1, nt, 0, 0)
			} else {
				res += dfs(pos+1, nt, 1, pc+dig)
			}
		}
		memo[kk] = res
		return res
	}
	return dfs(0, 1, 0, 0)
}

func bool64(b bool) int64 {
	if b {
		return 1
	}
	return 0
}
