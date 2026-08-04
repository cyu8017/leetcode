// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

func findMaxValueOfEquation(points [][]int, k int) int {
	type pair struct{ x, v int }
	q := []pair{}
	ans := int(-1e18)
	for _, p := range points {
		x, y := p[0], p[1]
		for len(q) > 0 && x-q[0].x > k {
			q = q[1:]
		}
		if len(q) > 0 {
			v := x + y + q[0].v
			if v > ans {
				ans = v
			}
		}
		value := y - x
		for len(q) > 0 && q[len(q)-1].v <= value {
			q = q[:len(q)-1]
		}
		q = append(q, pair{x, value})
	}
	return ans
}
