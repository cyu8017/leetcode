// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

func kthDistinct(arr []string, k int) string {
	freq := map[string]int{}
	for _, s := range arr {
		freq[s]++
	}
	for _, s := range arr {
		if freq[s] == 1 {
			k--
			if k == 0 {
				return s
			}
		}
	}
	return ""
}
