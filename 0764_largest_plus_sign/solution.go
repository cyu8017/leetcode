// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

func orderOfLargestPlusSign(n int, mines [][]int) int {
	banned := map[int]bool{}
	for _, m := range mines {
		banned[m[0]*n+m[1]] = true
	}
	arms := make([][]int, n)
	for i := range arms {
		arms[i] = make([]int, n)
	}
	best := 0
	for r := 0; r < n; r++ {
		count := 0
		for c := 0; c < n; c++ {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			arms[r][c] = count
		}
		count = 0
		for c := n - 1; c >= 0; c-- {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			if count < arms[r][c] {
				arms[r][c] = count
			}
		}
	}
	for c := 0; c < n; c++ {
		count := 0
		for r := 0; r < n; r++ {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			if count < arms[r][c] {
				arms[r][c] = count
			}
		}
		count = 0
		for r := n - 1; r >= 0; r-- {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			if count < arms[r][c] {
				arms[r][c] = count
			}
			if arms[r][c] > best {
				best = arms[r][c]
			}
		}
	}
	return best
}
