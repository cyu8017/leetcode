// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/


func minimumCost(s string) int64 {
	var ans int64
	n := len(s)
	for i := 1; i < n; i++ {
		if s[i] != s[i-1] {
			left := i
			right := n - i
			if left < right {
				ans += int64(left)
			} else {
				ans += int64(right)
			}
		}
	}
	return ans
}
