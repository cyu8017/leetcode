// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

func partitionString(s string) int {
	ans := 1
	seen := 0
	for i := 0; i < len(s); i++ {
		bit := 1 << (s[i] - 'a')
		if seen&bit != 0 {
			ans++
			seen = 0
		}
		seen |= bit
	}
	return ans
}
