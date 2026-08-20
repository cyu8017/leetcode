// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

func maximumGood(statements [][]int) int {
	n := len(statements)
	ans := 0
	ok := func(mask int) bool {
		for i := 0; i < n; i++ {
			if mask&(1<<i) == 0 {
				continue
			}
			for j := 0; j < n; j++ {
				s := statements[i][j]
				if s == 2 {
					continue
				}
				goodJ := mask&(1<<j) != 0
				if (s == 1 && !goodJ) || (s == 0 && goodJ) {
					return false
				}
			}
		}
		return true
	}
	for mask := 0; mask < 1<<n; mask++ {
		if ok(mask) {
			c := bitsCount2151(mask)
			if c > ans {
				ans = c
			}
		}
	}
	return ans
}

func bitsCount2151(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
