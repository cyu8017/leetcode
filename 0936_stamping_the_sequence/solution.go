// LeetCode 0936 - Stamping the Sequence
// https://leetcode.com/problems/stamping-the-sequence/

func movesToStamp(stamp string, target string) []int {
	n, m := len(target), len(stamp)
	done := make([]bool, n)
	ans := []int{}
	changed := true
	for changed {
		changed = false
		for i := n - m; i >= 0; i-- {
			ok := true
			anyUnset := false
			for j := 0; j < m; j++ {
				if !done[i+j] && target[i+j] != stamp[j] {
					ok = false
					break
				}
				if !done[i+j] {
					anyUnset = true
				}
			}
			if ok && anyUnset {
				for j := 0; j < m; j++ {
					done[i+j] = true
				}
				ans = append(ans, i)
				changed = true
				break
			}
		}
	}
	for _, d := range done {
		if !d {
			return []int{}
		}
	}
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return ans
}
