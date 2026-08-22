// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

func maxDifference(s string, k int) int {
	n := len(s)
	ans := int(-1e9)
	for a := 0; a < 5; a++ {
		for b := 0; b < 5; b++ {
			if a == b {
				continue
			}
			// max (freq_a - freq_b) with freq_a odd, freq_b even, len>=k
			prefA := make([]int, n+1)
			prefB := make([]int, n+1)
			for i := 0; i < n; i++ {
				prefA[i+1] = prefA[i]
				prefB[i+1] = prefB[i]
				if int(s[i]-'0') == a {
					prefA[i+1]++
				}
				if int(s[i]-'0') == b {
					prefB[i+1]++
				}
			}
			for i := 0; i < n; i++ {
				for j := i + k - 1; j < n; j++ {
					fa := prefA[j+1] - prefA[i]
					fb := prefB[j+1] - prefB[i]
					if fa%2 == 1 && fb%2 == 0 && fb > 0 {
						if fa-fb > ans {
							ans = fa - fb
						}
					}
				}
			}
		}
	}
	return ans
}
