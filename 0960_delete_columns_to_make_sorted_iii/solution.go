// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

func minDeletionSize(strs []string) int {
	m := len(strs[0])
	dp := make([]int, m)
	for i := range dp {
		dp[i] = 1
	}
	for j := 0; j < m; j++ {
		for i := 0; i < j; i++ {
			ok := true
			for _, row := range strs {
				if row[i] > row[j] {
					ok = false
					break
				}
			}
			if ok && dp[i]+1 > dp[j] {
				dp[j] = dp[i] + 1
			}
		}
	}
	mx := 0
	for _, v := range dp {
		if v > mx {
			mx = v
		}
	}
	return m - mx
}
