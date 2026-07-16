// LeetCode 0132 - Palindrome Partitioning II
func minCut(s string) int {
	n := len(s)
	pal := make([][]bool, n)
	for i := range pal { pal[i] = make([]bool, n) }
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			pal[i][j] = s[i] == s[j] && (j-i < 2 || pal[i+1][j-1])
		}
	}
	cuts := make([]int, n)
	for i := range s {
		cuts[i] = i
		for j := 0; j <= i; j++ {
			if pal[j][i] && (j == 0 || cuts[j-1]+1 < cuts[i]) {
				if j == 0 { cuts[i] = 0 } else { cuts[i] = cuts[j-1] + 1 }
			}
		}
	}
	return cuts[n-1]
}