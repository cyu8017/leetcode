// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

func isTransformable(s string, t string) bool {
	positions := make([][]int, 10)
	heads := make([]int, 10)
	for i := 0; i < len(s); i++ {
		d := int(s[i] - '0')
		positions[d] = append(positions[d], i)
	}
	for i := 0; i < len(t); i++ {
		d := int(t[i] - '0')
		if heads[d] >= len(positions[d]) {
			return false
		}
		index := positions[d][heads[d]]
		for smaller := 0; smaller < d; smaller++ {
			if heads[smaller] < len(positions[smaller]) && positions[smaller][heads[smaller]] < index {
				return false
			}
		}
		heads[d]++
	}
	return true
}
