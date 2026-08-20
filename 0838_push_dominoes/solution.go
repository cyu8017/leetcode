// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	force := make([]int, n)
	f := 0
	for i := 0; i < n; i++ {
		if dominoes[i] == 'R' {
			f = n
		} else if dominoes[i] == 'L' {
			f = 0
		} else if f > 0 {
			f--
		}
		force[i] += f
	}
	f = 0
	for i := n - 1; i >= 0; i-- {
		if dominoes[i] == 'L' {
			f = n
		} else if dominoes[i] == 'R' {
			f = 0
		} else if f > 0 {
			f--
		}
		force[i] -= f
	}
	out := make([]byte, n)
	for i, x := range force {
		if x > 0 {
			out[i] = 'R'
		} else if x < 0 {
			out[i] = 'L'
		} else {
			out[i] = '.'
		}
	}
	return string(out)
}
