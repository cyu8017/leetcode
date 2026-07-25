// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

func minPartitions(n string) int {
	best := 0
	for i := 0; i < len(n); i++ {
		d := int(n[i] - '0')
		if d > best {
			best = d
		}
	}
	return best
}
