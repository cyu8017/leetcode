// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

func countSteppingNumbers(low int, high int) []int {
	ans := []int{}
	if low == 0 {
		ans = append(ans, 0)
	}
	q := []int{}
	for i := 1; i <= 9; i++ {
		q = append(q, i)
	}
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		if x > high {
			continue
		}
		if x >= low {
			ans = append(ans, x)
		}
		last := x % 10
		if last > 0 {
			q = append(q, x*10+last-1)
		}
		if last < 9 {
			q = append(q, x*10+last+1)
		}
	}
	return ans
}
