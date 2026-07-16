// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

func countSegments(s string) int {
	count := 0
	inSegment := false
	for _, ch := range s {
		if ch != ' ' {
			if !inSegment {
				count++
				inSegment = true
			}
		} else {
			inSegment = false
		}
	}
	return count
}
