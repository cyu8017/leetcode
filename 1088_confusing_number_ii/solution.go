// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

func confusingNumberII(n int) int {
	rotate := map[int]int{0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
	digits := []int{0, 1, 6, 8, 9}
	ans := 0

	isConfusing := func(num int) bool {
		original := num
		rotated := 0
		for num > 0 {
			d := num % 10
			rotated = rotated*10 + rotate[d]
			num /= 10
		}
		return rotated != original
	}

	var dfs func(cur int)
	dfs = func(cur int) {
		if cur > n {
			return
		}
		if cur != 0 && isConfusing(cur) {
			ans++
		}
		if cur == 0 {
			for _, d := range []int{1, 6, 8, 9} {
				dfs(d)
			}
		} else {
			for _, d := range digits {
				dfs(cur*10 + d)
			}
		}
	}
	dfs(0)
	return ans
}
