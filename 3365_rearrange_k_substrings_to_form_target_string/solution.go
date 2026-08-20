// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

func isPossibleToRearrange(s string, t string, k int) bool {
	n := len(s)
	sz := n / k
	cnt := map[string]int{}
	for i := 0; i < n; i += sz {
		cnt[s[i:i+sz]]++
		cnt[t[i:i+sz]]--
	}
	for _, v := range cnt {
		if v != 0 {
			return false
		}
	}
	return true
}
