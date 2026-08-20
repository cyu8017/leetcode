// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

func minimumPartition(s string, k int) int {
	ans := 1
	cur := 0
	for i := 0; i < len(s); i++ {
		d := int(s[i] - '0')
		if d > k {
			return -1
		}
		nxt := cur*10 + d
		if nxt > k {
			ans++
			cur = d
		} else {
			cur = nxt
		}
	}
	return ans
}
