// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

func findDifferentBinaryString(nums []string) string {
	s := make(map[string]bool)
	for _, n := range nums {
		s[n] = true
	}
	n := len(nums)
	// Cantor's diagonalization
	ans := make([]byte, n)
	for i := 0; i < n; i++ {
		if nums[i][i] == '0' {
			ans[i] = '1'
		} else {
			ans[i] = '0'
		}
	}
	return string(ans)
}
