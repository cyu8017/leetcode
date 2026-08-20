// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

func powerfulIntegers(x int, y int, bound int) []int {
	ans := map[int]bool{}
	a := 1
	for a < bound {
		b := 1
		for a+b <= bound {
			ans[a+b] = true
			if y == 1 {
				break
			}
			b *= y
		}
		if x == 1 {
			break
		}
		a *= x
	}
	res := make([]int, 0, len(ans))
	for v := range ans {
		res = append(res, v)
	}
	return res
}
