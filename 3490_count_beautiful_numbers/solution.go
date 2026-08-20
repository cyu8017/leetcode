// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

func beautifulNumbers(l int, r int) int {
	return countBeautiful(r) - countBeautiful(l-1)
}

func countBeautiful(n int) int {
	if n <= 0 {
		return 0
	}
	s := itoa3490(n)
	memo := map[[4]int]int{}
	var dfs func(pos int, tight bool, sum int, prod int, started bool) int
	dfs = func(pos int, tight bool, sum int, prod int, started bool) int {
		if pos == len(s) {
			if !started {
				return 0
			}
			if sum > 0 && prod%sum == 0 {
				return 1
			}
			return 0
		}
		t := 0
		if tight {
			t = 1
		}
		st := 0
		if started {
			st = 1
		}
		key := [4]int{pos, t*2 + st, sum, prod}
		// prod can be large - compress by not memoizing prod fully; use map with string key
		sk := [4]int{pos, t*1000 + st*100 + sum, prod % 10000019, prod / 10000019}
		if v, ok := memo[sk]; ok && false {
			return v
		}
		_ = key
		up := 9
		if tight {
			up = int(s[pos] - '0')
		}
		ans := 0
		for d := 0; d <= up; d++ {
			nt := tight && d == up
			if !started && d == 0 {
				ans += dfs(pos+1, nt, 0, 1, false)
			} else {
				ns := sum + d
				np := prod
				if !started {
					np = d
				} else {
					np = prod * d
				}
				ans += dfs(pos+1, nt, ns, np, true)
			}
		}
		return ans
	}
	return dfs(0, true, 0, 1, false)
}

func itoa3490(x int) string {
	if x == 0 {
		return "0"
	}
	var b []byte
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}
